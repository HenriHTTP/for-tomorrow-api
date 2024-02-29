from flask import Flask
from routes.user.create_user_route import create_user_app
from routes.user.login_user_route import login_user_app
from routes.job.create_job_route import create_job_app

app = Flask(__name__)

app.register_blueprint(create_user_app)
app.register_blueprint(login_user_app)
app.register_blueprint(create_job_app)

if __name__ == '__main__':
    app.run(debug=True)
