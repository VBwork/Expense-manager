import json
import os

class Accounts:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def to_dict(self):
        account = {'name': self.name, 'balance': self.balance}
        return account


class AccountManager:
    file_accounts = 'accounts.json'

    def __init__(self):
        self.accounts = self.load_data_accounts()

    def add_accounts(self, account):
        self.accounts.append(account)
        self.save_data_accounts()

    def get_accounts(self):
        return self.accounts

    def add_balance(self, balance, account_id):
        account = self.accounts[account_id - 1]
        account.balance += balance
        self.save_data_accounts()

    def calculate_balance(self, balance, account_id):
        account = self.accounts[account_id - 1]
        account.balance -= balance
        self.save_data_accounts()

    def load_data_accounts(self):
        if os.path.exists(self.file_accounts):
            with open(self.file_accounts, 'r') as openfile:
                accounts = json.load(openfile)

        else:
            accounts = list()

        return accounts

    def save_data_accounts(self):
        save_accounts = json.dumps(self.accounts, default = lambda o: o.to_dict(), indent = 4)
        with open(self.file_accounts, 'w') as f:
            f.write(save_accounts)