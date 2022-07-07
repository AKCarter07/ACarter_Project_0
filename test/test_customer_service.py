from models.user import User
from service.customer_service import CustomerService
import pytest
from exception.invalid_parameter import InvalidParamError


def test_get_all_users(mocker):
    def mock_dao_get_all_users(self):
        user1 = User('user1', 1001)
        user1.set_num_active_accounts(2)
        user2 = User('user2', 1002)
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    cs = CustomerService()

    actual = cs.get_all_users()

    assert actual == [
        {
            'username': 'user1',
            'user_id': 1001,
            'num_active_accounts': 2,
            'active': True
        },
        {
            'username': 'user2',
            'user_id': 1002,
            'num_active_accounts': 1,
            'active': True
        }
    ]


def test_get_user_positive(mocker):
    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_get_user(self, user_id):
        if user_id == 1001:
            user1 = User('user1', 1001)
            user1.set_num_active_accounts(2)
            return user1
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_dao_get_user)
    cs = CustomerService()

    actual = cs.get_user(1001)

    assert actual == {
        'username': 'user1',
        'user_id': 1001,
        'num_active_accounts': 2,
        'active': True
    }


def test_get_user_negative(mocker):
    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_get_user(self, user_id):
        if user_id == 1001:
            user1 = User('user1', 1001)
            user1.set_num_active_accounts(2)
            return user1
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_dao_get_user)
    cs = CustomerService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = cs.get_user(1003)

    assert str(excinfo.value) == "User Id 1003 not found."


def test_add_user_positive(mocker):
    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_add_user(self, user_object):
        if user_object.get_idn() == 1003:
            return "User user3 (1003) has been added to the system"
        else:
            return None

    def mock_dao_number_idns(self):
        return 2

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.add_user', mock_dao_add_user)
    mocker.patch('dao.user_dao.UserDao.number_idns', mock_dao_number_idns)
    cs = CustomerService()

    actual = cs.add_user("user3")

    assert actual == 'User user3 (1003) has been added to the system'


def test_add_user_negative_spaces_short(mocker):
    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_add_user(self, user_object):
        print(user_object)
        if user_object.get_idn() == 1003:
            return f"User {user_object.get_username()} (1003) has been added to the system"
        else:
            return None

    def mock_dao_number_idns(self):
        return 2

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.add_user', mock_dao_add_user)
    mocker.patch('dao.user_dao.UserDao.number_idns', mock_dao_number_idns)
    cs = CustomerService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = cs.add_user(" sup")

    assert str(excinfo.value) == 'Username cannot contain spaces.\nUsername must be' \
                                 ' 5 or more characters.\n'

def test_add_user_negative_usn_taken(mocker):
    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_add_user(self, user_object):
        print(user_object)
        if user_object.get_idn() == 1003:
            return f"User {user_object.get_username()} (1003) has been added to the system"
        else:
            return None

    def mock_dao_number_idns(self):
        return 2

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.add_user', mock_dao_add_user)
    mocker.patch('dao.user_dao.UserDao.number_idns', mock_dao_number_idns)
    cs = CustomerService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = cs.add_user("user1")

    assert str(excinfo.value) == 'Username user1 already exists.\n'


def test_edit_user_positive(mocker):

    def mock_dao_edit_user(self, user_id, new_info_object):
        user = User('bobbert', 1001)
        user.set_num_active_accounts(2)
        return f"User has been updated: {user}"

    mocker.patch('dao.user_dao.UserDao.edit_user', mock_dao_edit_user)
    cs = CustomerService()

    user1 = User('bobbert', 1001)
    user1.set_num_active_accounts(2)

    actual = cs.edit_user(1001, user1)

    assert actual == 'User has been updated: \nbobbert (1001) has 2 active accounts: \n'


def test_dao_edit_user_negative(mocker):
    def mock_dao_edit_user(self, user_id, new_info_object):
        user = User('bobbert', 1002)
        user.set_num_active_accounts(2)
        return f"User has been updated: {user}"

    mocker.patch('dao.user_dao.UserDao.edit_user', mock_dao_edit_user)
    cs = CustomerService()

    user1 = User('bobbert', 2)
    user1.set_num_active_accounts(2)

    with pytest.raises(InvalidParamError) as excinfo:
        actual = cs.edit_user(1001, user1)

    assert str(excinfo.value) == 'Cannot change user Id.'

def test_dao_delete_user_positive(mocker):

    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_get_user(self, user_id):
        if user_id == 1001:
            user1 = User('user1', 1001)
            user1.set_num_active_accounts(2)
            return user1
        else:
            return None

    def mock_dao_delete_user(self, user_object):
        f"User account for {user_object.get_username()} has been deleted."

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_dao_get_user)
    mocker.patch('dao.user_dao.UserDao.delete_user', mock_dao_delete_user)
    cs = CustomerService()

    user1 = User('user1', 1001)
    user1.set_num_active_accounts(2)

    actual = cs.delete_user(user1)

    assert actual == f"All customer and account data for user1 " \
                     f"has been deleted."


def test_dao_delete_user_negative(mocker):

    def mock_dao_get_all_users(self):
        user1 = User('user1', '1001')
        user1.set_num_active_accounts(2)
        user2 = User('user2', '1002')
        user2.set_num_active_accounts(1)
        users = [user1, user2]
        return users

    def mock_dao_get_user(self, user_id):
        if user_id == 1001:
            user1 = User('user1', 1001)
            user1.set_num_active_accounts(2)
            return user1
        else:
            return None

    def mock_dao_delete_user(self, user_object):
        f"User account for {user_object.get_username()} has been deleted."

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_dao_get_all_users)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_dao_get_user)
    mocker.patch('dao.user_dao.UserDao.delete_user', mock_dao_delete_user)
    cs = CustomerService()

    user1 = User('user2', 1001)
    user1.set_num_active_accounts(2)

    with pytest.raises(InvalidParamError) as excinfo:
        actual = cs.delete_user(user1)

    assert str(excinfo.value) == "Cannot confirm user information."
