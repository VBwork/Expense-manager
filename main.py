import json
import os
from datetime import date

expenses = list()
categories = ['Food', 'Transport', 'Home', 'Close', 'Restoran']


def add_expense (money, comment, dt):
    expense = {'money': money, 'comment': comment, "date": dt}
    expenses.append(expense)


def add_category (name):
    categories.append(name)


def load_data_expense(file_expenses):
    global expenses

    if os.path.exists(file_expenses):
        with open('expenses.json', 'r') as openfile:
            expenses = json.load(openfile)

    return expenses


def load_data_categories(file_categories):
    global categories

    if os.path.exists(file_categories):
        with open('categories.json', 'r') as openfile:
            categories = json.load(openfile)

    return categories


def menu(expenses, categories):

    while True:
        acction = input('Оберіть дію:\n1 - Додати витрату;\n2 - Додати витрату за минулий період;\n3 - Список категорій;\n4 - Додати категорію;\n5 - Статистика витрат; \n6 - Вийти\n')

        if acction == '1':
            add_expense(input('Введіть суму витрати: '), input('Додайте коментар до витрати: '), str(date.today()))

        elif acction == '2':
            add_expense(input('Введіть суму витрати: '), input('Додайте коментар до витрати: '), input('Введіть дату витрати: '))

        elif acction == '3':
            print(categories)

        elif acction == '4':
            add_category(input('Введіть назву категорії: '))

        elif acction == '5':
            print(expenses)

        else:
            print('Роботу завершено')

            break

        save_data_expenses(expenses)
        save_data_categories(categories)


def save_data_expenses(expenses):
    save_expenses = json.dumps(expenses)

    with open('expenses.json', 'w') as f:
        f.write(save_expenses)


def save_data_categories(categories):
    save_categories = json.dumps(categories)

    with open('category.json', 'w') as f:
        f.write(save_categories)


def main():
    file_expenses = 'expenses.json'

    file_categories = 'categories.json'

    expenses = load_data_expense(file_expenses)

    categories = load_data_categories(file_categories)

    menu(expenses, categories)


if __name__ == '__main__':
    main()