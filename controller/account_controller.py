from flask import Blueprint, request
from models.account import Account
from service.account_service import AccountService
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParamError


ac = Blueprint('account_controller', __name__)
account_service = AccountService()
customer_service = CustomerService()

@ac.route ('/users/<user_id>/accounts')
def get_user_accounts(user_id):
    try:
        return account_service.get_accounts(user_id), 201
    except InvalidParamError as e:
        return {
            "message": f"{e}"
        }, 400


@ac.route('/users/<user_id>/accounts/<account_number>')
def get_user_account(user_id, account_number):
    try:
        return account_service.get_account(user_id, account_number), 201
    except InvalidParamError as e:
        return {
                   "message": f"{e}"
               }, 400

@ac.route('/users/<user_id>/accounts/<account_number>', methods=['PUT'])
def edit_account(user_id, account_number):
    user_json_dict = request.get_json()
    try:
        if user_json_dict['action'] == 'withdraw':
            return account_service.withdraw(user_id, account_number, user_json_dict['dollars'],
                                            user_json_dict['cents']), 201
        elif user_json_dict['action'] == 'deposit':
            return account_service.deposit(user_id, account_number, user_json_dict['dollars'],
                                            user_json_dict['cents']), 201
        else:
            return f"Action {user_json_dict['action']} not valid. Please check spelling.", 400
    except InvalidParamError as e:
        return {
                   "message": f"{e}"
               }, 400

@ac.route ('/users/<user_id>/accounts',  methods=['POST'])
def add_account(user_id):
    user_json_dict = request.get_json()
    try:
        return account_service.add_account(user_id, user_json_dict['dollars'], user_json_dict['cents'])
    except InvalidParamError as e:
        return {
                   "message": f"{e}"
               }, 400


@ac.route('/users/<user_id>/accounts/<account_number>', methods=['DELETE'])
def delete_account(user_id, account_number):
    try:
        return account_service.delete_account(user_id, account_number)
    except InvalidParamError as e:
        return {
                   "message": f"{e}"
               }, 400

