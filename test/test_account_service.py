from service.account_service import AccountService
from pytest_mock import mocker

acs = AccountService()

def test_get_accounts():
    # Arrange
    def mock_get_accounts(self):
        return {'10010001': {'account number': '10010001', 'dollars': 25, 'cents': 25},
                '10010002': {'account number': '10010002', 'dollars': 100, 'cents': 50}}

    mocker.mock('acs.AccountDao.get_accounts', mock_get_accounts())
    # Act

    # Assert