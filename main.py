from flask import Flask
from routes.create_user_rote import create_user_app

app = Flask(__name__)

app.register_blueprint(create_user_app)

if __name__ == '__main__':
    app.run(debug=True)
