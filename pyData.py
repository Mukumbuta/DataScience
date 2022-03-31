Categories = {}

import sys

class Budget:

    def __init__(self, category, amount):
        self.category  = category
        self.amount    = amount

    def deposit_funds(amount, bal):
        bal += amount
        return bal

    def withdraw_funds(user, amount, bal):
        bal -=  amount
        return bal

    def compute_balance(Categories):
        for categ, bal in Categories.items():
            print(categ, bal)


def init():
    print("><><><><><> Budget Manager <><><><><><\n")
            
    menu_items()


def menu_items():
    selected_category = int(input("><><><>< Select your option ><><><><>< \n1. Create New Category\n2. Deposit funds \n3. Withdraw Funds\n4. Transfer Funds\n5. Check Balance\n6. Exit \n"))
    
    if(selected_category == 1):
        create_category()

    if(selected_category == 2):
        credit_category()

    elif(selected_category == 3):
        debit_category()

    elif(selected_category == 4):
        transfer_funds()

    elif(selected_category == 5):
       bal_check()

    elif(selected_category == 6):
        sys.exit()
        print("Thank you for using Budget Manager")

    else:
        print("You have selected an invalid option")

        menu_items()


def create_category():
    print("\n><><><>< Create New Category ><><><><>< \n")

    budget_title = input("Enter category name:\n")

    amount = int(input("Enter amount: \n$"))

    category= Budget(budget_title, amount)
    Categories[budget_title] = amount

    print(" ")
    print(f'{budget_title} category created successfully with ${amount}')
    
    menu_items()


def debit_category():
    print("<<*>> Withdraw Section <<*>>")
    print("<<>>> Budget Categories <<>>")

    for key,value in Categories.items():
        print("# {}".format(key))

    user_response = int(input("\nDo you want to continue with transaction? \n1. YES \n2. NO\n"))
    if user_response == 1:
        selected_category = input("\n<<<>>> Select a category to withdraw from <<<>>>\n")
    
    if selected_category in Categories.keys():
        amount = int(input("Enter amount: \n$ "))

        if amount < Categories[selected_category]:
            bal = int(Categories[selected_category])
            bal = Budget.withdraw_funds(selected_category, bal, amount)
            Categories[selected_category] = bal
            
            print("Withdraw of ${} from {} category is successful".format(amount, selected_category))
            print("Your balance is now ${}".format(bal))

            menu_items()


def credit_category():
    print(">>><<< Deposit Section >>><<<")
    print(">>><< Budget Categories >><<<")

    for key,value in Categories.items():
        print("# {}".format(key))

        user_choice = input(">><< Select a category to deposit to >><<\n")
        if user_choice in Categories.keys():

            amount = int(input("Enter amount:\n$ "))
            bal = int(Categories[user_choice])
            bal = Budget.deposit_funds(amount, bal)

            print("{} has been credited with ${}".format(user_choice, amount))
            print("Your new bal is now ${}".format(bal))

            menu_items()
 

def transfer_funds():
    print(">>><<<Welcome to the money transfer section>>><<<")
    

def bal_check():
    check_bal_for = input("Enter a category to check balance\n")

    for check_bal_for in Categories.items():
        Budget.compute_balance(Categories)
        
init()
