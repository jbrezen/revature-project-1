from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.login import Login
from services.login_service import LoginService


def route(app):
    @app.route("/login/", methods=['POST'])
    def post_login():
        req = Login.parse_json(request.json)
        new_req = LoginService.create_login(req)
        return jsonify(new_req.json()), 201

    @app.route("/login/", methods=['GET'])
    def all_logins():
        return jsonify(LoginService.all_logins()), 200

    @app.route("/login/<login_id>/", methods=['GET'])
    def get_login(login_id):
        try:
            req = LoginService.get_login(login_id)
            return jsonify(req.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/login/<login_id>/", methods=['PUT'])
    def update_login(login_id):
        try:
            req = Login.parse_json(request.json)
            req.login_id = login_id
            response = LoginService.update_login(req)
            return jsonify(response), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/login/<login_id>/", methods=['DELETE'])
    def delete_login(login_id):
        return LoginService.delete_login(login_id), 204
