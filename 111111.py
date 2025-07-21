import json
import os
from datetime import date

class Expense:
    def __init__(self, money, comment, dt):
        self.money = money
        self.comment = comment
        self.dt = dt

    def to_dict(self):
        expense = {'money': self.money, 'comment': self.comment, "date": self.dt}
        return expense


class ExpensesManager:
    file_expenses = 'expenses.json'

    def __init__(self):
        self.expenses = self.load_data_expense()

    def add_expense (self, expense):
        self.expenses.append(expense)
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


class CategoryManager:
    file_categories = 'categories.json'

    def __init__(self):
        self.categories = self.load_data_categories()

    def add_category(self, category):
        self.categories.append(category)
        self.save_data_categories()

    def get_categories(self):
        return self.categories

    def load_data_categories(self):

        if os.path.exists(self.file_categories):
            with open(self.file_categories, 'r') as openfile:
                categories = json.load(openfile)
        else:
            categories = ['Food', 'Transport', 'Home', 'Close', 'Restoran']

        return categories

    def to_dict(self):
        return self.categories

    def save_data_categories(self):
        save_categories = json.dumps(self.categories, default = lambda o: o.to_dict(), indent = 4)

        with open(self.file_categories, 'w') as f:
            f.write(save_categories)


class Category:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        category = self.name
        return category

    def __repr__(self):
        return self.name

def menu():

    expenses_manager = ExpensesManager()
    categories_manager = CategoryManager()

    while True:
        acction = input('Оберіть дію:\n1 - Додати витрату;\n2 - Додати витрату за минулий період;\n3 - Список категорій;\n4 - Додати категорію;\n5 - Статистика витрат; \n6 - Вийти\n')

        if acction == '1':
            expense = Expense(input('Введіть суму витрати: '), input('Додайте коментар до витрати: '), str(date.today()))
            expenses_manager.add_expense(expense)

        elif acction == '2':
            expense = Expense(input('Введіть суму витрати: '), input('Додайте коментар до витрати: '), input('Введіть дату витрати: '))
            expenses_manager.add_expense(expense)

        elif acction == '3':
            print(categories_manager.get_categories())

        elif acction == '4':
            category = Category(input('Введіть назву категорії: '))
            categories_manager.add_category(category)

        elif acction == '5':
            print(expenses_manager.get_expenses())

        else:
            print('Роботу завершено')

            break


def main():

    menu()


if __name__ == '__main__':
    main()