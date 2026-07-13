# # Single Inheritance


# class Collage:
#     def fun(self):
#         print("collage name is: SITRC")

# class Student(Collage):
#     def student_info(self, name, roll_no):
#         print("Student name is: ", name)
#         print("Student roll.no: ", roll_no)

    
# obj = Student()
# obj.fun()
# obj.student_info("Deven", "32")




# # multilevel inheritance

# class Collage:
#     def fun(self):
#         print("Collage name is: SITRC") 

# class Student(Collage):
#     def student_info(self, name, branch):
#         print("Name: ", name)
#         print("Branch: ", branch)

# class Exam(Student):
#     def subject(self, sub1, sub2, sub3):
#         print("Subject1: ", sub1)
#         print("Subject1: ", sub2)
#         print("Subject1: ", sub3)

# obj = Exam()
# obj.fun()
# obj.student_info("Deven", "Comp")
# obj.subject("M1", "M2", "M3")



# # multiple inheritance

# class submarks:
#     math = int(input("enter the marks got in math: "))
#     DE = int(input("enter the marks got in DE: "))
#     c = int(input("enter the marks got in c language: "))    
#     english = int(input("enter the marks got in english: "))

# class pracMarks:
#     cpract = int(input("enter the marks got in practical: "))

# class result(submarks, pracMarks):
#     def total(self):
#         if(self.math > 40 and self.DE > 40 and self.c > 40 and self.english > 40 and self.cpract > 20):
#             print("pass")
#         else:
#             print("fail")

# obj = result()
# obj.total()    







# examples:

class TandP:
    def training(self):
        pass
    def placement(self):
        pass

class Deven(TandP):
    def training(self):
        print("Python")
    def placement(self):
        print("python | django")
        print()

class Aryan(TandP):
    def training(self):
        print("Java Training")
    def placement(self):
        print("Java Development")
        print()

class Riya(TandP):
    def training(self):
        print("HTML/CSS Training")
    def placement(self):
        print("Web Development")
        print()

obj = Deven()
obj.training()
obj.placement()
obj = Aryan()
obj.training()
obj.placement()
obj = Riya()
obj.training()
obj.placement()
