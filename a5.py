import os
import platform
import time

#making a clear console function for clean console
def clear_console():
    # Determine the operating system
    operating_system = platform.system()

    # Clear console based on the operating system
    if operating_system == 'Windows':
        os.system('cls')
    elif operating_system in ['Linux', 'Darwin']:
        os.system('clear')


saving_balance = 2500.54
checking_balance = 1500.32

while True:
    print("#" * 80)
    print("                          Welcome to Nolan's ATM")
    print("#" * 80)

    print("Input: 1 - Check balance | Input: 2 - Deposit | Input: 3 - Withdrawal")
    menu_option = input("What are we doing here today? ")
    clear_console()
    if menu_option == '1':
        user_account_name = input("What is your account name? (Input your name or 'exit' to leave) ")
        if user_account_name.lower() == 'exit':
            break
        else:
            clear_console()
            print("Choose account type:")
            print("Input: 1 - Savings | Input: 2 - Checking")
            account_type = input("Enter your choice: ")

            if account_type == '1':
                print("Your current savings balance is ${:.2f}".format(saving_balance))
            elif account_type == '2':
                print("Your current checking balance is ${:.2f}".format(checking_balance))
            else:
                print("Invalid choice. Please enter 1 or 2.")
            time.sleep(6)
            clear_console()
        
    elif menu_option == '2':
        user_account_name = input("What is your account name? (Input your name or 'exit' to leave) ")
        if user_account_name.lower() == 'exit':
            break
        else:
            clear_console()
            print("Choose account type:")
            print("Input: 1 - Savings | Input: 2 - Checking")
            account_type = input("Enter your choice: ")
            clear_console()
            if account_type == '1':
                deposit_amount = float(input("How much would you like to deposit? (e.g., 400.40) "))
                if deposit_amount > 0:
                    saving_balance += deposit_amount
                    print("Your new savings balance is ${:.2f}".format(saving_balance))
                else:
                    print("Invalid deposit amount. Please enter a positive value.")
            elif account_type == '2':
                deposit_amount = float(input("How much would you like to deposit? (e.g., 400.40) "))
                if deposit_amount > 0:
                    checking_balance += deposit_amount
                    print("Your new checking balance is ${:.2f}".format(checking_balance))
                else:
                    print("Invalid deposit amount. Please enter a positive value.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
            clear_console()

    elif menu_option == '3':
        user_account_name = input("What is your account name? (Input your name or 'exit' to leave) ")
        if user_account_name.lower() == 'exit':
            break
        else:
            print("Choose account type:")
            print("Input: 1 - Savings | Input: 2 - Checking")
            account_type = input("Enter your choice: ")

            if account_type == '1':
                withdrawal_amount = float(input("How much would you like to withdraw? (e.g., 200.20) "))
                if withdrawal_amount > 0 and withdrawal_amount <= saving_balance:
                    saving_balance -= withdrawal_amount
                    print("Your new savings balance is ${:.2f}".format(saving_balance))
                elif withdrawal_amount > saving_balance:
                    print("Insufficient funds. Your current savings balance is ${:.2f}".format(saving_balance))
                else:
                    print("Invalid withdrawal amount. Please enter a positive value.")
            elif account_type == '2':
                withdrawal_amount = float(input("How much would you like to withdraw? (e.g., 200.20) "))
                if withdrawal_amount > 0 and withdrawal_amount <= checking_balance:
                    checking_balance -= withdrawal_amount
                    print("Your new checking balance is ${:.2f}".format(checking_balance))
                elif withdrawal_amount > checking_balance:
                    print("Insufficient funds. Your current checking balance is ${:.2f}".format(checking_balance))
                else:
                    print("Invalid withdrawal amount. Please enter a positive value.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
