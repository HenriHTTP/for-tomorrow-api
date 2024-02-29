from flask import Blueprint, request, jsonify
from entities.job import Job
from usecases.job.create_job.implements import create_job_controller


create_job_app = Blueprint('create_job', __name__)


@create_job_app.route('/create_job', methods=['POST'])
async def create_job_route():
    http_request = Job(
        job_title=request.json.get("job_title"),
        company=request.json.get("company"),
        about_company=request.json.get("about_company"),
        localization=request.json.get("localization"),
        job_type=request.json.get("job_type"),
        job_description=request.json.get("job_description"),
        requirements=request.json.get("requirements")
    )
    try:
        http_response = await create_job_controller.create_job(http_request)
        return jsonify({
            "message": http_response.message,
            "error": http_response.error,
            "status": http_response.status_code,
            "success": http_response.success
        })
    except Exception as error:
        return jsonify({
            "message": "User not created",
            "error": str(error),
            "status": 500,
            "success": False
        }), 500

