from flask import Blueprint, request
from models.user import User
from service.account_service import AccountService
from service.customer_service import CustomerService



uc = Blueprint('user_controller', __name__)
account_service = AccountService()
customer_service = CustomerService()

@uc.route('/users')
def get_all_users():
    return {
        "users": customer_service.get_all_users()  # a list of dictionaries
    }

@uc.route('/users/<username>')
def get_user_by_username(username):
    try:
        return user_service.get_user_by_username(username)  # dictionary
    except KeyError as e:
        return {
            "message": f"User with username {username} was not found!"
        }, 404