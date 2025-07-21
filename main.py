from datetime import date
from Account import *
from Exspense import *
from Category import *

def menu():
    expenses_manager = ExpensesManager()
    categories_manager = CategoryManager()
    accounts_manager = AccountManager()

    while True:
        acction = input('Оберіть дію:\n1 - Аккаунти;\n2 - Додати аккаунт;\n3 - Додати витрату;\n4 - Додати витрату за минулий період;\n5 - Статистика витрат;'
                        '\n6 - Список категорій;\n7 - Додати категорію;\n8 - Вийти\n')

        if acction == '1':
            print(accounts_manager.get_accounts())

        elif acction == '2':
            account = Accounts(input('Введіть назву аккаунту: '), input('Введіть cуму балансу: '))
            accounts_manager.add_accounts(account)

        elif acction == '3':
            expense = Expense(input('Введіть суму витрати: '), input(f'Оберіть аккаунт: {accounts_manager.get_accounts()}'),
                              input('Додайте коментар до витрати: '), str(date.today()))
            expenses_manager.add_expense(expense)

        elif acction == '4':
            expense = Expense(input('Введіть суму витрати: '), input('Додайте коментар до витрати: '), input('Введіть дату витрати: '))
            expenses_manager.add_expense(expense)

        elif acction == '5':
            print(expenses_manager.get_expenses())

        elif acction == '6':
            print(categories_manager.get_categories())

        elif acction == '7':
            category = Category(input('Введіть назву категорії: '))
            categories_manager.add_category(category)

        else:
            print('Роботу завершено')

            break


def main():

    menu()


if __name__ == '__main__':
    main()