# from abc import ABC,abstractmethod
# class Help4code(ABC): #abstract class
#     @abstractmethod # decorator
#     def training(self): # abstract method
#         pass

#     @abstractmethod     #abstract method
#     def placement(self):
#         pass

# class Ashish(ABC):
#     def training(self):
#         print('c,c++,java')

#     def placement(self):
#         print("java placement")    

# class Ankush(ABC):
#     def training(self):
#         print('pythom | django')

#     def placement(self):
#         print("pyhton placements students ")        


# class Aditya(ABC):
#     def training(self):
#         print('Machine Learning')

#     def placement(self):
#         print("Data Science Placement")

# obj1 = Ashish()
# obj1.training()
# obj1.placement()           

# obj2 = Ankush()
# obj2.training()
# obj2.placement()

# obj3 = Aditya()
# obj3.training()
# obj3.placement()


from abc import ABC,abstractmethod
class irctc(ABC):
    @abstractmethod
    def bookTicket(self):
        pass 

class MakemyTrip(irctc):    
    def bookTicket(self):
        print("=======================================")
        print("         Welcome To MakeMyTrip            ")
        self.source = input("Enter a source station :")
        self.destination = input("Enter a destination name : ")
        self.date = input("Enter data ")


class Goibibo(irctc):
    def bookTicket(self):
        print("Welcome to Goibibo") 


class Yatra(irctc):
    def bookTicket(self):
        print("Welcome to yatra.com")           

m = MakemyTrip()
m.bookTicket()
g = Goibibo()
g.bookTicket()
y = Yatra()
y.bookTicket()    