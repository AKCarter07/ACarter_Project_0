from flask import Blueprint, request
from models.user import User
from service.account_service import AccountService
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParamError


uc = Blueprint('user_controller', __name__)
account_service = AccountService()
customer_service = CustomerService()

@uc.route('/users')
def get_all_users():
    return {
        "users": customer_service.get_all_users()  # a list of dictionaries
    }

@uc.route('/users/<user_id>')
def get_user_by_id(user_id):
    try:
        return customer_service.get_user(user_id)  # dictionary
    except InvalidParamError as e:
        return {
            "message": f"{e}"
        }, 404

@uc.route('/users', methods=['POST'])
def add_user():
    user_json_dict = request.get_json()
    try:
        return customer_service.add_user(user_json_dict['username']), 201
    except InvalidParamError as e:
        return {
            "message": f"{e}"
        }, 400

@uc.route('/users/<user_id>', methods=['PUT'])
def edit_user_by_id(user_id):
    user_json_dict = request.get_json()
    user_object = User(user_json_dict['username'], user_json_dict['user_id'])
    user_object.set_num_active_accounts(user_json_dict['num_accounts'])
    user_object.set_status(user_json_dict['active'])
    try:
        return customer_service.edit_user(user_id, user_object), 201
    except InvalidParamError as e:
        return {
                "message": f"{e}"
                }, 400

@uc.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_json_dict = request.get_json()
    if user_id == user_json_dict['user_id']:
        user_object = User(user_json_dict['username'], user_json_dict['user_id'])
        user_object.set_num_active_accounts(user_json_dict['num_accounts'])
        user_object.set_status(user_json_dict['active'])
        user_object.set_accounts(user_json_dict['accounts'])
        try:
            return customer_service.delete_user(user_object), 201
        except InvalidParamError as e:
            return {
                    "message": f"{e}"
                   }, 400
    else:
        print("Something has gone wrong with the delete user operation "
              "from the user controller module. Please contact IT to "
              "resolve this issue.")
