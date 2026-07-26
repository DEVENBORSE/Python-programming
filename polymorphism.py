#python does not support constructor overloading
# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# class Arithmetic:
#     def __init__(self):
#         print("There is no Argument")
#     def __init__(self, a):
#         print("passing one argument")
#     def __init__(self, a,b):
#         print("passing 2 arguments")

# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(10,20)

#overiding

# class Rbi:
#     def homeloan(self):
#         print("Home loan rate of interest 8%")
#     def carloan(self):
#         print("car loan rate of interest 7%")

# class Sbi(Rbi):
#     def homeloan(self):
#         print("Home loan rate of interest 10.5%")
#         super().homeloan() # super() keyword
# sbiObj = Sbi()
# sbiObj.homeloan()

class Father:
    def __init__(self):
        print("Father: I am already at breakfast table")

class Child(Father):
    def __init__(self):
        print("child: i will be at breakfast table")
        super().__init__()
obj = Child()