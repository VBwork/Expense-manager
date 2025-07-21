from datetime import date
from Account import *
from Exspense import *
from Category import *

def menu():
    expenses_manager = ExpensesManager()
    categories_manager = CategoryManager()
    accounts_manager = AccountManager()

    while True:
        acction = input('Оберіть дію:\n1 - Аккаунти;\n2 - Додати аккаунт;\n3 - Видалити аккаунт;\n4 - Додати витрату;\n5 - Додати витрату за минулий період;\n6 - Статистика витрат;'
                        '\n7 - Список категорій;\n8 - Додати категорію;\n9 - Видалити категорію;\n10 - Вийти\n')

        if acction == '1':
            print(accounts_manager.get_accounts())

        elif acction == '2':
            account = Accounts(input('Введіть назву аккаунту: '), input('Введіть cуму балансу: '))
            accounts_manager.add_accounts(account)

        elif acction == '3':
            accounts_manager.del_account(input(f'Оберіть аккаунт: {accounts_manager.get_accounts()}'))

        elif acction == '4':
            expense = Expense(input('Введіть суму витрати: '), input(f'Оберіть аккаунт: {accounts_manager.get_accounts()}'),
                              input('Додайте коментар до витрати: '), str(date.today()))
            expenses_manager.add_expense(expense)

        elif acction == '5':
            expense = Expense(input('Введіть суму витрати: '), input('Додайте коментар до витрати: '), input('Введіть дату витрати: '))
            expenses_manager.add_expense(expense)

        elif acction == '6':
            print(expenses_manager.get_expenses())

        elif acction == '7':
            print(categories_manager.get_categories())

        elif acction == '8':
            category = Category(input('Введіть назву категорії: '))
            categories_manager.add_category(category)

        elif acction == '9':
            categories_manager.del_category(input(f'Оберіть категорію: {categories_manager.get_categories()}'))

        else:
            print('Роботу завершено')

            break


def main():

    menu()


if __name__ == '__main__':
    main()