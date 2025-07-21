import json
import os

class Expense:
    def __init__(self, money, account_id, comment, dt):
        self.money = money
        self.comment = comment
        self.dt = dt
        self.account_id = account_id

    def to_dict(self):
        expense = {'money': self.money, 'comment': self.comment, "date": self.dt}
        return expense


class ExpensesManager:
    file_expenses = 'expenses.json'

    def __init__(self):
        self.expenses = self.load_data_expense()

    def add_expense (self, expense, account_manager):
        self.expenses.append(expense)
        account_manager.calculate_balance(expense.money, expense.account_id)
        self.save_data_expenses()

    def get_expenses(self):
        return self.expenses

    def load_data_expense(self):

        if os.path.exists(self.file_expenses):
            with open(self.file_expenses, 'r') as openfile:
                expenses = json.load(openfile)
        else:

            expenses = list()

        return expenses

    def save_data_expenses(self):
        save_expenses = json.dumps(self.expenses, default = lambda o: o.to_dict(), indent = 4)

        with open(self.file_expenses, 'w') as f:
            f.write(save_expenses)
