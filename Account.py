class Account:
    def get_data(self):

        self.acc_no = int(input("Enter the account number: "))
        self.name = input("Enter the name: ")
        self.bal = int(input("Enter the balance: "))
        print()


    def show_data(self):
        print(f"The account number of the acc. Holder: {self.acc_no} ")
        print(f"The name of the acc. Holder: {self.name} ")
        print(f"The Balance of the acc. Holder: {self.bal} ")


obj = Account()
obj.get_data()
obj.show_data()