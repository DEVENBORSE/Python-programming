# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Aditya"
#         self.__c = "Ashish"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class : ")
#         # print(self.a)
#         # print(self.__c)

# # obj1 = Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2 = Base()
# print(obj2.a)
# print(obj2.__c)



# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Aditya"
#         self._c = "Ashish"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class : ")
#         print(self.a)
#         print(self.__c)

# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)


class Rbi:
    def publicPolicy(self):
        print("Check the public policy of RBI")

    def __privatePolicy(self):
        print("There is some private policy which is not accessible for public ")

class Sbi(Rbi):
    def  __init__(self):
        Rbi.__init__(self)

    def callingPublicMethod(self):
        print("\n inside child class")
        self.publicPolicy()

    def callingPriavteMethod(self):
        self.__privatePolicy()

# obj1 = Rbi()
# obj1.callingPublicMethod()
# obj1.callingPriavteMethod()

# obj1.publicPolicy()
# obj1.__privatePolicy() 

obj2 = Rbi()
obj2.publicPolicy()
obj2._Rbi__privatePolicy()


#destructor  : deallocates the memory 