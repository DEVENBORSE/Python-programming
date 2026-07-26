#inheritance : 
#1) single inheritance : when a child class inherits from a single parent class
# class College:
#     def collegename(self):
#         print("Modern College of Engineering, Pune")

# class Student(College):
#     def details(self):
#         print("Student of Modern College of Engineering, Pune")

# obj = Student()
# obj.collegename()
# obj.details()

#2) multilevel inheritance : when a child class inherits from a parent class and the parent class inherits from another parent class
# class College:
#     def collegename(self):
#         print("Modern College of Engineering, Pune")
# class Student(College):
#     def details(self):
#         print("Student of Modern College of Engineering, Pune")
# class Exam(Student):
#     def examdetails(self):
#         print("Subject1 : MATHS")
#         print("Subject1 : DSA")                
# obj = Exam()
# obj.collegename()
# obj.details()
# obj.examdetails()        

#3) Multiple inheritance : 
#  syntax : 
# class SubMarks:
#     math = int(input("Enter marks of math : "))
#     DE = int(input("Enter marks of DE : "))
#     c = int(input("Enter marks of c : "))
#     English = int(input("Enter marks of english : "))
# class practmarks:
#     cpract = int(input("Enter marks of cpract : "))
# class Result(SubMarks,practmarks):
#     def total(self):
#         if self.math>40 and self.DE > 40  and self.c>40 and self.English > 40 and self.cpract > 20 :
#             print("pass")
#         else:
#             print("fail")
# obj = Result()
# obj.total()      

# class A:
#     def add(self):
#         print("addition")
# class B:
#     def add(self):
#         print("addition1")
# class C(A,B) :                             
#     def b(self):
#         print("success")
# c = C()
# c.add()

