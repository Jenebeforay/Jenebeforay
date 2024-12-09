class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. Current balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


def main():
    print("Welcome to the Bank Account Simulator!")
    name = input("Enter the account owner's name: ")
    account = BankAccount(name)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using the Bank Account Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
