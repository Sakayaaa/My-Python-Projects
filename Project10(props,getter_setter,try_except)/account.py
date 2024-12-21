from validator import *


class Account:
    def __init__(self, title, account_id, amount):
        self.title = title
        self.account_id = account_id
        self.amount = amount

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title= title_validator(value)


    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = account_id_validator(value)


    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = amount_validator(value)


    def __repr__(self):
        return str(self.__dict__)


