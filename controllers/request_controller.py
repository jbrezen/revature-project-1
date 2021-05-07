from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.request import Request
from services.request_service import RequestService


def route(app):
    @app.route("/request/", methods=['POST'])
    def post_request():
        req = Request.parse_json(request.json)
        new_req = RequestService.create_request(req)
        return jsonify(new_req.json()), 201

    @app.route("/request/", methods=['GET'])
    def all_requests():
        return jsonify(RequestService.all_requests()), 200

    @app.route("/request/<request_id>/", methods=['GET'])
    def get_request(request_id):
        try:
            req = RequestService.get_request(request_id)
            return jsonify(req.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/request/<request_id>/", methods=['PUT'])
    def update_request(request_id):
        try:
            req = Request.parse_json(request.json)
            req.request_id = request_id
            response = RequestService.update_request(req)
            return jsonify(response.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/request/<request_id>/", methods=['DELETE'])
    def delete_request(request_id):
        return RequestService.delete_request(request_id), 204
