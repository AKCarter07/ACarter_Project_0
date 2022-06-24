from models.user import User

users = {}
users.update({"u1": User("user1", 1001)})
users.update({"u2": User("user2", 1002)})
users.update({'u3': User("user3", 1003)})
users['u1'].add_account(789.2)
users['u1'].add_account(1002)
users['u2'].add_account(502.73)


class UserDao:

    def get_usernames(self, username):
        return users[username]

    def get_all_users(self):
        user_values = []
        for value in users.values():
            user_values.append(value)
        return user_values

    def add_user(self, user_object):
        users[user_object.username] = user_object
        return user_object

    def edit_user(self, username, new_user_info_object):
        if username == new_user_info_object.username:
            users[username] = new_user_info_object
        else:
            del users[username]
            users[new_user_info_object.username] = new_user_info_object
        return new_user_info_object
