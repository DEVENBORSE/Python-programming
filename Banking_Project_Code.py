class BankAccount:     
    def __init__(self, account_number, account_holder, balance=0):         
        self.account_number = account_number         
        self.account_holder = account_holder         
        self.__balance = balance  

    # Encapsulated attribute (private)      
    def deposit(self, amount):         
        if amount > 0:             
            self.__balance += amount             
            print(f"Deposited {amount}. New balance: {self.__balance}")         
        else:             
            print("Deposit amount must be positive.")      

    def withdraw(self, amount):         
        if amount > 0 and amount <= self.__balance:             
            self.__balance -= amount             
            print(f"Withdrew {amount}. New balance: {self.__balance}")         
        else:             
            print("Insufficient balance or invalid amount.")      

    def check_balance(self):         
        print(f"Current balance: {self.__balance}")   




class SavingsAccount(BankAccount):     

    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):         
        super().__init__(account_number, account_holder, balance)         
        self.interest_rate = interest_rate      

    def add_interest(self):         
        interest = self._BankAccount__balance * self.interest_rate         
        self.deposit(interest)        
        print(f"Added interest of {interest}. New balance: {self._BankAccount__balance}")   



class CurrentAccount(BankAccount): 
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500): 
        super().__init__(account_number, account_holder, balance) 
        self.overdraft_limit = overdraft_limit 

    def withdraw(self, amount): 
        if amount > 0 and (self._BankAccount__balance - amount) >= -self.overdraft_limit: 
            self._BankAccount__balance -= amount 
            print(f"Withdrew {amount}. New balance: {self._BankAccount__balance}") 
        else: print("Withdrawal exceeds overdraft limit or invalid amount.")



# Example usage 
account1 = SavingsAccount("12345", "Jadu", 1000) 
account1.deposit(500) 
account1.add_interest() 
account1.check_balance() 

account2 = CurrentAccount("67890", "pakya", 500) 
account2.withdraw(200) 
account2.check_balance() 
account2.withdraw(900)  # Exceeds overdraft limit 