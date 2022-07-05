from dao.user_dao import UserDao
from exception.invalid_parameter import InvalidParamError
from models.user import User


class CustomerService:
    def __init__(self):
        self.user_dao = UserDao()

    def user_id_list(self):
        users = self.user_dao.get_all_users()
        user_ids = []
        for user in users:
            if user.get_status():
                user_ids.append(user.get_idn())
        return user_ids

    def get_all_users(self):
        list_user_objects = self.user_dao.get_all_users()
        user_dictionaries = []
        for user_obj in list_user_objects:
            user_dictionaries.append(user_obj.to_dict())
        return user_dictionaries

    def get_user(self, user_id):
        id_list = self.user_id_list()
        if f'{user_id}' not in id_list:
            raise InvalidParamError(f"User Id {user_id} not found.")
        user_obj = self.user_dao.get_user(user_id)
        return user_obj.to_dict()

    def add_user(self, username):
        users = self.user_dao.get_all_users()
        usernames = []
        user_ids = []
        idn = 1000 + self.user_dao.number_idns() + 1
        for user in users:
            usernames.append(user.get_username())
            user_ids.append(user.get_idn())
        good_to_go = True
        error_message = ""

        if username in usernames:
            good_to_go = False
            error_message += f"Username {username} already exists.\n"
        if idn in user_ids:
            good_to_go = False
            error_message += f"User id {idn} already exists.\n"

        if " " in username:
            good_to_go = False
            error_message += "Username cannot contain spaces.\n"
        if len(username) < 5:
            good_to_go = False
            error_message += "Username must be 5 or more characters.\n"

        if not len(str(idn)) == 4:
            good_to_go = False
            error_message += "User ID must be 4 digits.\n"

        if good_to_go:
            added_user_object = self.user_dao.add_user(User(username, idn))
            return added_user_object
        else:
            raise InvalidParamError(error_message)

    def edit_user(self, user_id, user_object):
        if user_id != user_object.get_idn():
            raise InvalidParamError("Cannot change user Id.")
        edited_user = self.user_dao.edit_user(user_id, user_object)
        return edited_user

    def delete_user(self, user_object):
        check_user = self.get_user(user_object.get_idn())
        print(user_object.to_dict())
        print(check_user)
        if str(user_object.to_dict()) != str(check_user):
            raise InvalidParamError("Cannot confirm user information.")
        self.user_dao.delete_user(user_object)
        return f"All customer and account data for {user_object.get_username()} " \
               f"has been deleted."
