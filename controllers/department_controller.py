from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.department import Department
from services.department_service import DepartmentService


def route(app):
    @app.route("/department/", methods=['POST'])
    def post_department():
        req = Department.parse_json(request.json)
        new_req = DepartmentService.create_department(req)
        return jsonify(new_req.json()), 201

    @app.route("/department/", methods=['GET'])
    def all_departments():
        return jsonify(DepartmentService.all_departments()), 200

    @app.route("/department/<department_id>/", methods=['GET'])
    def get_department(department_id):
        try:
            req = DepartmentService.get_department(department_id)
            return jsonify(req.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department/<department_id>/", methods=['PUT'])
    def update_department(department_id):
        try:
            req = Department.parse_json(request.json)
            req.department_id = department_id
            response = DepartmentService.update_department(req)
            return jsonify(response), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department/<department_id>/", methods=['DELETE'])
    def delete_department(department_id):
        return DepartmentService.delete_department(department_id), 204
