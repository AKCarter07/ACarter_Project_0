from flask import Flask
from controller.user_controller import uc
import psycopg
from models.user import User


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(uc)
    app.run(port=8080, debug=True)



