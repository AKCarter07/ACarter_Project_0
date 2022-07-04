from flask import Flask
from controller.user_controller import uc
from controller.account_controller import ac
import psycopg
from models.user import User


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(uc)
    app.register_blueprint(ac)
    app.run(port=8080, debug=True)



