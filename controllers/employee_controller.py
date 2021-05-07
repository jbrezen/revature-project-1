from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from services.employee_service import EmployeeService


def route(app):
    @app.route("/employee/", methods=['POST'])
    def post_employee():
        req = Employee.parse_json(request.json)
        new_req = EmployeeService.create_employee(req)
        return jsonify(new_req.json()), 201

    @app.route("/employee/", methods=['GET'])
    def all_employees():
        return jsonify(EmployeeService.all_employees()), 200

    @app.route("/employee/<employee_id>/", methods=['GET'])
    def get_employee(employee_id):
        try:
            req = EmployeeService.get_employee(employee_id)
            return jsonify(req.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employee_id>/", methods=['PUT'])
    def update_employee(employee_id):
        try:
            req = Employee.parse_json(request.json)
            req.employee_id = employee_id
            response = EmployeeService.update_employee(req)
            return jsonify(response), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employee_id>/", methods=['DELETE'])
    def delete_employee(employee_id):
        return EmployeeService.delete_employee(employee_id), 204
