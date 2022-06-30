from dao.user_dao import UserDao
from exception.invalid_parameter import InvalidParamError


class CustomerService:
    def __init__(self):
        self.__user_dao = UserDao()

    def get_all_users(self):
        list_user_objects = self.__user_dao.get_all_users()
        user_dictionaries = []
        for user_obj in list_user_objects:
            user_dictionaries.append(user_obj.to_dict())
        return user_dictionaries

    def get_user(self, username):
        user_obj = self.__user_dao.get_user(username)
        return user_obj.to_dict()

    def add_user(self, user_object):
        if " " in user_object.get_username():
            raise InvalidParamError("Username cannot contain spaces")

        if len(user_object.get_username()) < 5:
            raise InvalidParamError("Username must be 5 or more characters.")

        add_user_object = self.__user_dao.add_user(user_object)
        return add_user_object.to_dict()

    def edit_user(self, username, user_object):
        edited_user = self.__user_dao.edit_user(username, user_object)
        return edited_user.to_dict()
