class BankAccount:
    def __init__(self, account_number, account_holder_name, balance, branch):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.branch = branch
    #displaying the account details
    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Balance:", self.balance)
        print("Branch:", self.branch)
    #depositing the amount
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    #withdrawing the amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")
account = BankAccount("101", "Akshaya", 25000, "Hyderabad")
print("Original Account Details:")
account.display_account_details()
account.deposit(5000)
account.withdraw(3000)
print("\nUpdated Account Details:")
account.display_account_details()
