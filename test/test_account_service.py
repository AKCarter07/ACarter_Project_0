import service.customer_service
from service.account_service import AccountService
from models.user import User
from models.account import Account
from dao.user_dao import UserDao
import pytest
from exception.invalid_parameter import InvalidParamError


def test_get_accounts(mocker):
    # Arrange
    def mock_get_accounts(self, user_id):
        if user_id == 1001:
            return {'10010001': {'account number': '10010001', 'dollars': 10, 'cents': 10},
                    '10010002': {'account number': '10010002', 'dollars': 10, 'cents': 10}}
        else:
            return None

    def mock_dao_get_user(self, user_id):
        if user_id == 1001:
            user1 = User('user1', 1001)
            user1.add_account(10, 10)
            user1.add_account(10, 10)
            return user1
        else:
            return None

    def mock_acct_dao_get_account(self, account_id, user_id):
        return Account(account_id, 10, 10)

    mocker.patch('dao.account_dao.AccountDao.get_user_accounts', mock_get_accounts)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_dao_get_user)
    mocker.patch('dao.account_dao.AccountDao.get_account', mock_acct_dao_get_account)
    acs = AccountService()
    # Act
    actual = acs.get_accounts(1001)

    # Assert
    assert actual == {'10010001': {'account number': '10010001', 'cents': 10, 'dollars': 10},
                      '10010002': {'account number': '10010002', 'cents': 10, 'dollars': 10}}

def test_get_account_positive(mocker):
    def mock_cs_user_list(self):
        return ['1001', '1002']

    def mock_get_accounts(self, user_id):
        if user_id == 1001:
            return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                    '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}
        else:
            return None

    def mock_get_account(self, user_id, account_id):
        return Account(10010001, 25, 25)

    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('service.customer_service.CustomerService.user_id_list', mock_cs_user_list)
    mocker.patch('dao.account_dao.AccountDao.get_user_accounts', mock_get_accounts)
    mocker.patch('dao.account_dao.AccountDao.get_account', mock_get_account)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)
    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)
    acs = AccountService()

    actual = acs.get_account(1001, 10010001)

    assert actual == {'account number': '10010001', 'cents': 25, 'dollars': 25}

def test_get_account_bad_user_id(mocker):
    def mock_cs_user_list(self):
        return ['1001', '1002']

    def mock_get_accounts(self, user_id):
        if user_id == 1001:
            return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                    '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}
        else:
            return None

    def mock_get_account(self, user_id, account_id):
        return Account(10010001, 25, 25)

    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('service.customer_service.CustomerService.user_id_list', mock_cs_user_list)
    mocker.patch('dao.account_dao.AccountDao.get_user_accounts', mock_get_accounts)
    mocker.patch('dao.account_dao.AccountDao.get_account', mock_get_account)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)
    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)
    acs = AccountService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = acs.get_account(1003, 10010001)

    assert str(excinfo.value) == 'User Id does not exist.'

def test_get_account_neg_acct_not_found(mocker):
    def mock_cs_user_list(self):
        return ['1001', '1002']

    def mock_get_accounts(self, user_id):
        if user_id == 1001:
            return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                    '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}
        else:
            return None

    def mock_get_account(self, user_id, account_id):
        return Account(10010001, 25, 25)

    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('service.customer_service.CustomerService.user_id_list', mock_cs_user_list)
    mocker.patch('dao.account_dao.AccountDao.get_user_accounts', mock_get_accounts)
    mocker.patch('dao.account_dao.AccountDao.get_account', mock_get_account)
    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)
    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)
    acs = AccountService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = acs.get_account(1001, 10010003)

    assert str(excinfo.value) == 'Account 10010003 not found.'


def test_withdraw_positive(mocker):
    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_edit_account(self, account_id, user_id, operation, dollars, cents):
        if account_id == 10010001:
            dollars = 25 - dollars
            cents = 25 - cents
            account = Account(10010001, dollars, cents)
            return account
        else:
            return None

    mocker.patch('dao.account_dao.AccountDao.edit_account', mock_edit_account)

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)

    acs = AccountService()
    actual = acs.withdraw(1001, 10010001, 10, 10)

    assert actual == "New balance: Account 10010001: Balance $15.15"

def test_withdraw_neg_id_not_found(mocker):
    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_edit_account(self, account_id, user_id, operation, dollars, cents):
        if account_id == 10010001:
            dollars = 25 - dollars
            cents = 25 - cents
            account = Account(10010001, dollars, cents)
            return account
        else:
            return None

    mocker.patch('dao.account_dao.AccountDao.edit_account', mock_edit_account)

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)

    acs = AccountService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = acs.withdraw(1001, 10010003, 10, 10)
    assert str(excinfo.value) == "Account 10010003 not found."

def test_withdraw_neg_insufficient_funds(mocker):
    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_edit_account(self, account_id, user_id, operation, dollars, cents):
        if account_id == 10010001:
            dollars = 25 - dollars
            cents = 25 - cents
            account = Account(10010001, dollars, cents)
            return account
        else:
            return None

    mocker.patch('dao.account_dao.AccountDao.edit_account', mock_edit_account)

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)

    acs = AccountService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = acs.withdraw(1001, 10010001, 100, 10)
    assert str(excinfo.value) == "You do not have sufficient funds."

def test_deposit_positive(mocker):
    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_edit_account(self, account_id, user_id, operation, dollars, cents):
        if account_id == 10010001:
            dollars = 25 + dollars
            cents = 25 + cents
            account = Account(10010001, dollars, cents)
            return account
        else:
            return None

    mocker.patch('dao.account_dao.AccountDao.edit_account', mock_edit_account)

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)

    acs = AccountService()
    actual = acs.deposit(1001, 10010001, 10, 10)

    assert actual == "New balance: Account 10010001: Balance $35.35"

def test_deposit_neg_id_not_found(mocker):
    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_edit_account(self, account_id, user_id, operation, dollars, cents):
        if account_id == 10010001:
            dollars = 25 + dollars
            cents = 25 + cents
            account = Account(10010001, dollars, cents)
            return account
        else:
            return None

    mocker.patch('dao.account_dao.AccountDao.edit_account', mock_edit_account)

    def mock_get_accounts_via_user(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.patch('models.user.User.get_accounts', mock_get_accounts_via_user)

    acs = AccountService()

    with pytest.raises(InvalidParamError) as excinfo:
        actual = acs.withdraw(1001, 10010003, 10, 10)
    assert str(excinfo.value) == "Account 10010003 not found."

def test_add_account(mocker):

    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_create_account(self, user_id, account_id, dollars, cents):
        return f"Account {account_id} created with a starting balance of ${dollars}." \
               f"{'0' if cents < 10 else ''}{cents}"

    mocker.patch('dao.account_dao.AccountDao.create_account', mock_create_account)

    def mock_dao_edit_user(self, user_id, new_info_object):
        user = User('bobbert', 1001)
        user.set_num_active_accounts(2)
        return f"User has been updated: {user}"

    mocker.patch('dao.user_dao.UserDao.edit_user', mock_dao_edit_user)

    acs = AccountService()

    actual = acs.add_account(1001, 10, 10)

    assert actual == 'Account 10010003 created with a starting balance of $10.10'

def test_delete_account_positive(mocker):
    def mock_get_user_accounts(self, user_id):
        user1 = User('user1', 1001)
        user1.add_account(25, 25)
        user1.add_account(100, 50)
        return user1

    mocker.patch('dao.user_dao.UserDao.get_user', mock_get_user_accounts)

    def mock_cs_user_id_list(self):
        return ['1001', '1002']

    mocker.patch('service.customer_service.CustomerService.user_id_list', mock_cs_user_id_list)

    def mock_delete_account(self, user_id, account_id):
        return f"Account {account_id} has been deleted."

    def mock_dao_edit_user(self, user_id, new_info_object):
        return f"User has been updated: {new_info_object}"

    mocker.patch('dao.user_dao.UserDao.edit_user', mock_dao_edit_user)

    acs = AccountService()

    actual = acs.delete_account(1001, 10010001)

    assert actual == 'Account 10010001 has been deleted.'
