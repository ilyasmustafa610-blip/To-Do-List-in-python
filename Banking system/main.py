class BankAcccount:

    # initailize account with pin and history

    def __init__(self , name , pin , balance=0):

        self.name = name

        self.pin = pin

        self.balance = balance

        self.history = []

    # Desposit Money

    def desposit(self , amount):

        self.history += amount

        self.history.append(f"Desposited ${amount}")

        print(f"{amount} Desposited! New Balance ${self.balance}")

    # withdrawl money

    def withdraw(self , amount):

        if amount <= self.balance:

            self.balance -= amount

            self.history.append(f"Withdrawl! ${amount}")
        
            print(f"${amount} Withdraw! New Balance ${self.balance}")

        else:

            print("Insuffecient Balance!")

    # show balance

    def show_balance(self):

        print(f"Account Holder:{self.name} , Balance:{self.balance}")

    # show transection history

    def show_history(self):

        print("\n--- Transection History ---")

        for t in self.history:

            print(t) if self.history else print("No Transection in this..")


    #  Main program

name=input("Enter your name:")

pin=input("Enter 4-digit pin:")

account = BankAcccount(name ,  pin)

#  ask for pin before access

if input("Enter PIN to login:") != account.pin:

    print("Wrong PIN! Reenter your pin")

    exit()

while True:

    print("\n 1.Desposit 2.Withdrawl 3.Show balance 4.History 5.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        
        account.desposit(int(input("Enter amount:")))
    
    elif choice == "2":

        account.withdraw(int(input("Enter amount:")))

    elif choice == "3":

        account.show_balance()

    elif choice == "4":

        account.show_history()

    elif choice == "5":

        print("Thankyou for your kind!")

        break
    
    else:

        print("Enter a valid choice")

    
