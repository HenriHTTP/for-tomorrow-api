from flask import Blueprint, request, jsonify
from usecases.user.login_user.implements import login_user_controller
from entities.user import User

login_user_app = Blueprint('Login_user_route', __name__)


@login_user_app.route('/Login_user_route', methods=['POST'])
async def login_user_route():
    http_request = User(
        name=None,
        lastname=None,
        email=request.json.get("email"),
        password=request.json.get("password"),
        username=None
    )
    http_response = await login_user_controller.login_user(http_request)
    try:
        if http_response:
            return jsonify({
                "message": http_response.message,
                "error": http_response.error,
                "status": http_response.status_code,
                "success": http_response.success,
                "token": http_response.token
            }), 200
    except Exception as error:
        return jsonify({
            "message": "User not created",
            "error": str(error),
            "status": 500,
            "success": False
        }), 500
