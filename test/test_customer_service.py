from models.user import User
from service.customer_service import CustomerService
import pytest


# def test_get_all_users(mocker):
#     print("\nin mocker")
#
#     def mock_dao_get_all_users():
#         user1 = User('user1', 1001)
#         user1.set_num_active_accounts(2)
#         user2 = User('user2', 1002)
#         user2.set_num_active_accounts(1)
#         users = [user1, user2]
#         return users
#
#     mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users())
#     cs = CustomerService()
#
#     actual = cs.get_all_users()
#     print("printing actual")
#     print(actual)
#     assert actual == [1, 2]


    # assert actual == [
    #     {
    #         'username': 'user1',
    #         'user_id': 1001,
    #         'num_active_accounts': 2,
    #         'active': True
    #     },
    #     {
    #         'username': 'user2',
    #         'user_id': 1002,
    #         'num_active_accounts': 1,
    #         'active': True
    #     }
    # ]


def test_add_user_positive(mocker):
    def mock_add_user(username):
