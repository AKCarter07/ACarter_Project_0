from dao.user_dao import UserDao
from exception.invalid_parameter import InvalidParamError
from exception.already_exists import AlreadyExistsError


class CustomerService:
    def __init__(self):
        self.__user_dao = UserDao()

    def get_all_users(self):
        list_user_objects = self.__user_dao.get_all_users()
        user_dictionaries = []
        for user_obj in list_user_objects:
            user_dictionaries.append(user_obj.to_dict())
        return user_dictionaries

    def get_user(self, user_id):
        user_obj = self.__user_dao.get_user(user_id)
        return user_obj

    def add_user(self, user_object):
        users = self.__user_dao.get_all_users()
        usernames = []
        user_ids = []
        for user in users:
            usernames.append(user.get_username())
            user_ids.append(user.get_idn())

        if user_object.get_username() in usernames:
            raise AlreadyExistsError(f"Username {user_object.get_username()} already exists.")
        if user_object.get_idn in user_ids:
            raise AlreadyExistsError(f"User id {user_object.get_idn()} already exists.")

        if " " in user_object.get_username():
            raise InvalidParamError("Username cannot contain spaces")
        if len(user_object.get_username()) < 5:
            raise InvalidParamError("Username must be 5 or more characters.")

        if not len(user_object.get_idn()) == 4:
            raise InvalidParamError("User ID must be 4 digits.")

        add_user_object = self.__user_dao.add_user(user_object)
        return add_user_object

    def edit_user(self, user_id, user_object):
        if user_id != user_object.get_idn():
            raise InvalidParamError("Cannot change user Id.")
        edited_user = self.__user_dao.edit_user(user_id, user_object)
        return edited_user

    def delete_user(self, user_object):
        check_user = self.get_user(user_object.get_idn())
        if str(user_object) != str(check_user):
            raise InvalidParamError("Cannot confirm user information.")
        self.__user_dao.delete_user(user_object)
        return f"All customer and account data for {user_object.get_username()} " \
               f"has been deleted."
