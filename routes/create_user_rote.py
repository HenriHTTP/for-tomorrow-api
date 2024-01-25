from flask import Blueprint, request, jsonify
from usecases.user.implements import create_user_controller
from entities.user import User

create_user_app = Blueprint('create_user_app', __name__)


@create_user_app.route('/create_user_rote', methods=['POST'])
async def create_user_rote():
    http_request = User(
        name=request.json.get("name"),
        lastname=request.json.get("lastname"),
        email=request.json.get("email"),
        password=request.json.get("password"),
        username=request.json.get("username")
    )
    http_response = await create_user_controller.create_user(http_request)
    if http_response.success:
        return jsonify({
            "message": http_response.message,
            "error": http_response.error,
            "status": http_response.status_code,
            "success": http_response.success
        }), 200
    else:
        return jsonify({
            "message": http_response.message,
            "error": http_response.error,
            "status": http_response.status_code,
            "success": http_response.success
        }), 500
