__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

class Customer:
    def __init__(self, name, surname, tc_identification, phone_number):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone_number = phone_number
    
    def display_information(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"TC Identification: {self.tc_identification}")
        print(f"Phone Number: {self.phone_number}")
        
class Account():
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Balance: {self.balance}")
        
first_customer = Customer("John", "Doe", "12345678901", "+1234567890")
first_account = Account("1234567890", 1000, first_customer)

first_account.customer.display_information()
first_account.display_balance()
first_account.deposit(500)
first_account.withdraw(200)