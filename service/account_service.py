from dao.user_dao import UserDao


class AccountService:
    def __init__(self):
        self.__user_dao = UserDao()

    def get_all_users(self):
        list_user_objects = self.__user_dao.get_all_users()
        user_dictionaries = []
        for user_obj in list_user_objects:
            user_dictionaries.append(user_obj.to_dict())
        return user_dictionaries