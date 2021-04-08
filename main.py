import sqlite3

db = sqlite3.connect('budget.s3db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS budget
(food INTEGER DEFAULT 0,
clothing INTEGER DEFAULT 0,
entertainment INTEGER DEFAULT 0);''')

global food, clothing, entertainment
items = ['food', 'clothing', 'entertainment']
options = {1: 'food', 2: 'clothing', 3: 'entertainment'}


class Budget:

    def __init__(self):
        sql.execute(f'INSERT INTO budget(food, clothing, entertainment) VALUES (0, 0, 0) ')
        db.commit()


    def deposit(self, category, amount):
        if category in items:
            sql.execute(f'UPDATE budget SET {category} = {category} + {amount}')
            db.commit()

    def withdraw(self, category, amount):
        if category in items:
            sql.execute(f'UPDATE budget SET {category} = {category} - {amount}')
            db.commit()

    def transfer(self, category1, category2, amount):
        if category1 in items and category2 in items:
            sql.execute(f'UPDATE budget SET {category1} = {category1} - {amount}')
            sql.execute(f'UPDATE budget SET {category2} = {category2} + {amount}')
            db.commit()

    def balance(self, category):
        if category in items:
            sql.execute(f'SELECT {category} from budget')
            bal = sql.fetchone()
            print(bal)


def welcome_menu():
    print('''What would like to do:
1. Make a deposit
2. Make a withdrawal
3. Make a transfer
4. Check balance
5. Exit''')


def options_menu():
    print('''1. Food
2. Clothing
3. Entertainment''')

def withdraw_menu():
    print('From which category would you like to withdraw:')
    options_menu()

def transfer_menu():
    print('From which categories do you want to transfer:')
    options_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        welcome_menu()
        myBudget = Budget()
        choice = int(input('> '))
        if choice == 1:
            options_menu()
            deposit_to = int(input('> '))
            deposit_amount = int(input('Enter amount: '))
            myBudget.deposit(options[deposit_to], deposit_amount)
        elif choice == 2:
            withdraw_menu()
            withdraw_from = int(input('> '))
            withdraw_amount = int(input('Enter amount: '))
            myBudget.withdraw(options[withdraw_from], withdraw_amount)
        elif choice == 3:
            transfer_menu()
            transfer_from = int(input('Transfer from: '))
            transfer_to = int(input('Transfer to: '))
            transfer_amount = int(input('Enter amount: '))
            myBudget.transfer(options[transfer_from], options[transfer_to], transfer_amount)
        elif choice == 4:
            options_menu()
            balance_cat = int(input('Enter category: '))
            myBudget.balance(options[balance_cat])
        elif choice == 5:
            break
