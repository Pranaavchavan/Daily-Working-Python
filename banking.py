
pin = 1212
userPin = int(input("Enter your pin: "))
if userPin == pin:
    print("Welcome to Patil Bank")
    print("""
    1. Deposit
    2. Withdraw Money
    3. Check Balance
    4. Exit
    """)
    balance = 5000
    choice = int(input("Enter your choice: ")) 
    if choice == 1:
        deposit = int(input("Enter amount to be deposited: "))
        if deposit > 0:
            balance += deposit
            print("Rs", deposit, "has been deposited successfully. New balance: Rs", balance)
        else:
            print("Invalid amount")
    elif choice == 2:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw > 0:
            if withdraw <= balance:
                balance -= withdraw
                print("Rs", withdraw, "withdrawn successfully. New balance: Rs", balance)
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")
    elif choice == 3:
        print("Your balance is: Rs", balance)
    elif choice == 4:
        print("Exit")
        print("tahnk you for banking with us")
    else:
        print("Invalid choice")
else:
    print("Invalid pin")
    
    
    
