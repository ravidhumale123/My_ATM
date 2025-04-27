import time as t

pin_code = 1148
balance = 1000000

def main_fun():
    while True:
        print(" 0 - Exit")
        print(" 1 - Check balance")
        print(" 2 - Withdraw money")
        print(" 3 - Deposit money")
        print(" 4 - Change pin code")
        print(" 5 - Return ATM card")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exitting...😕")
            t.sleep(2)
            print("you have been logged out")
            print("\n")
            break

        if authenticate():
            if choice == 1:                
                check_balance()
            elif choice == 2:
                draw_amount()
            elif choice == 3:
                deposit_amount()
            elif choice == 4:
                change_pin()
            elif choice == 5:
                return_ATM()
                



def authenticate():
    num_attempts = 3
    while num_attempts > 0:

        input_pin = int(input("Enter your pin code: "))
        print("Verifying pin code...")
        t.sleep(1.5)
        
        if pin_code == input_pin:
            return True
        else:
            print("Incorrect pin code. Please try again.")
            num_attempts -= 1
            print(f'you have {num_attempts} more attempts left....')
            print("\n")


def check_balance():
    print("fetching account balance...")
    t.sleep(2.5)
    print("Your current balance is: ", balance)
    print("\n")


def draw_amount():
    global balance
    print("processing cash withdrawal...")
    t.sleep(2.5)

    while True:
        withdraw = int(input("Enter the amount to withdraw : "))
        if withdraw > balance:
            print("Insufficient Balance")
        else:
            print("Please wait, your transaction is proceding...")
            t.sleep(2.5)
            print(f'you have entered {withdraw}')
            confirm = input("Entered amount is correct...?\n")

            if confirm in ('Y','y','yes','Yes'):
                balance -= withdraw
                print("Please take your cash...")
                t.sleep(2.5)
                print("Transaction successful")
                print("\n")
            else:
                print("Transaction cancelled")
                t.sleep(2.5)
                print("Please take your card...")
            break


def deposit_amount():
    global balance
    print("processing cash deposit...")
    t.sleep(2.5)

    while True:
        deposit = int(input("Enter amount to deposit: "))
        if deposit <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            print("Please wait, your transaction is proceeding...")
            t.sleep(2)
            print(f'you have entered {deposit}')
            confirm = input("Entered amount is correct...?\n")

            if confirm in ('Y','y','yes','Yes'):
                balance += deposit
                print("Transaction successful")
                t.sleep(2.5)
                print("Please take your card...")
                print(" thank you for using our ATM service...")
                print("\n")
            else:
                print("Transaction cancelled")
                t.sleep(2.5)
                print("Please take your card...")
            break


def change_pin():
    global pin_code
    print("processing pin code change...")
    t.sleep(2.5)

    while True:
        new_pin = int(input("Enter new pin code: "))
        if len(str(new_pin)) != 4:
            print("Invalid pin code. Please enter a 4-digit number.")
        else:
            print("Please wait, your transaction is proceeding...")
            t.sleep(2)
            print(f'you have entered {new_pin}')
            confirm = input("Entered new pin code is correct...?\n")

            if confirm in ('Y','y','yes','Yes'):
                pin_code = new_pin
                print("Pin code changed successfully")
                t.sleep(2.5)
                print("Please take your card...")
                print(" thank you for using our ATM service...")
                print("\n")
            else:
                print("Transaction cancelled")
                t.sleep(2.5)
                print("Please take your card...")
            break

def return_ATM():
    print("processing ATM card return...")
    t.sleep(2.5)
    print("Please take your card...")
    t.sleep(2.5)
    print("thank you for using our ATM service...")
    print("\n")

main_fun()