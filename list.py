# 
# myList = ["prashant","Aditya","jai","Ahmed",77,"sandip",60.52,"prakash"]
# print(myList)
# print(type(myList))
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[-1])
# print(myList[2:5])
# print(myList[:])
# print(myList[1:])
# print(myList[1:8:2])
# print(myList[::-1])
# myList[2] = "Akshay"
# print(myList)

# if "Ahmed" in myList:
#     print("Yes its available")
# else:
#     print("Not available")

# myList.append('harsh')
# myList.append('laxman')
# print(myList)

# myList.insert(1,'Sanket')
# print(myList)

# myList.remove("sandip")
# print(myList)

# newlist = myList.copy()
# print(newlist)



# myList = [["Aditya",45],["Prathmesh","Aakash"],["Johnny sins",69.69]]
# print("Example of multidimensional list : ")
# print(myList)
# print(myList[0][0])
# print(myList[0][1])
# print(myList[1][1])
# print(myList[1][0])
# print(myList[2][0])

# list1 = ["prashant","jha"]
# # print(list1*2)
# list2 = [50,25.50]
# print(list1+list2)

# list2 = [50,25.50,'prashant']
# del list2
# print(list2)

# list2 = [50,25.50,'prashant']
# list2.clear()
# print(list2)


# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)

# mylist = [44,22,77,0,8]
# mylist.sort()
# print(mylist)

# mylist1 = [44,55,66,90,1,3]
# mylist1.sort(reverse=True)
# print(mylist1)


#list alising: 
# mylist = [44,0,22,33]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0] = "prashant"
# print(mylist)
# print(newlist)


#loops for list : 
# memberhip operator :  1) in 2)not in
# name = "help4code"
# print("h"in name)
# print("z"in name)
# print("z" not in name)

# for i in range(5):
#     print(i)

# for j in range(1,5):
#     print(j)

# for k in range(1,10,2):
#     print(k)

# for i in range(5,-1,-1):
#     print(i)

# for i in range(1,11):
    
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
#     print("-----------------------------")
#     for j in range(1,11):
#         print(j*11," ",j*12)
  
# list3 = [10,20,30,40,50]

# for i in list3:
#     print(i)


# list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for x in list:
#     sum = sum + x
# print("The sum = ",sum)


# myCart = [10,20,200,300,800,60,700]
# for i in myCart:
#     if i > 400:
#         print("My purchased cart item")
#         break        #continue
#     print(i)


# count = 0
# for i in range(9):
#     if i %2==0:
#         print(i)
#     else:
#         print(i)
#         count+=1
# print("Count= ",count)  


# rollno = [ 3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
#         print("even no is found",x)
#         break

# print("enter day : ")
# day = input()
# if day == 'saturday' or day =='sunday':
#     print("Its weekend")
# else:
#     print("Its not weekend")    

# num = 123
# a = num % 10
# num = num // 10
# b = num % 10
# num = num //10
# c = num % 10
# num = num // 10
# rev = a*100 + b*10 + c *1
# print(rev)


# num1 = 1234567
# a =  num1 % 10
# num1 = num1 // 10
# b = num1 % 10
# num1 = num1 // 10
# c = num1 % 10
# num1 = num1 // 10
# d = num1 % 10
# num1 = num1 // 10
# e = num1 % 10
# num1 = num1 // 10
# f = num1 % 10
# num1 =  num1 // 10
# g = num1 % 10
# num1 = num1 // 10
# rev1 = a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 + g*1
# print(rev1)


# Amount = int(input("Enter amount: "))
# print("100 notes = ",Amount//100)
# print("50 notes = ",(Amount%100)//50)
# print("20 notes = ",((Amount%100))%50//20)
# print("10 notes = ",(((Amount%100)%50)%20)//10)
# print("5 notes = ",((((Amount%100)%50)%20)%10)//5)


# age1  = int(input("Enter age of 1st person: "))
# age2 = int(input("Enter age of 2nd person:"))
# age3 = int(input("Enter age of 3rd person:"))
# if age1>age2 :
#     if age1>age3:
#          print("1st person is largest")
#     else:
#         print("3rd person is largest")
# else:
#     if age2>age3:
#         print("2nd person is largest")
#     else:
#         print("3rd person is largest")


# char = input("Enter character:")
# if len(char)!= 1:
#     print("print exactly one character")
# else:
#     ascii_val= ord(char)
# if 65<= ascii_val <=90:
#     print("Uppercase")
# elif 97<= ascii_val<= 122:
#     print("Lowercase")
# elif 48<= ascii_val<= 57:
#     print("Digits")
# else:
#     print("Special symbol")


# while True:
#     username = input("Enter username: ")
#     password = input("Enter password : ")
# if username == password:
#     print("Succesful login")
# else:
#     print("Invalid login")


# find( ) return starting index number of string if it is found else if string doesn't exist then it returns -1

# s = "prashant","aditya","sandip"
# m = '|'.join(s)
# print(m)

# s = "python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print("Subject Marks: ")
# phy = 50
# chem = 60
# maths = 70
# print("physics={} chemistry={} Maths={}".format(phy,chem,maths))
# print("physics={0} chemistry={1} Maths={2}".format(phy,chem,maths))
# print("physics={x} chemistry={y} Maths={z}".format(x=phy,y=chem,z=maths))
# total = phy + chem + maths
# print("total mark {total}")
# print("roll no=","7".zfill(4))


# name = "help4code"
# for i in name:
#     print(i)


# name = "prashant"
# i = 0
# for x in name:
#     if x =='n':
#         print("THE CHARACTER FOUND AT ",i,"value=",x)
#         break
#     i = i + 1

# a = 'shiwaleew'
# for i in a:
#     if i  == 'w':
#         print(i)

# x = ['x','y','z']
# y = ['x','y','z']
# z = [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)
# x = x.append('k')
# print(x == y)


# a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)


# s =""
# s1 = s.replace("difficult","easy")
# print(s1)


# s = 'abababaabababa'
# s2 = s.replace("a","b")
# print(s2)

s = 'gasgg54@#vscsd!s*'
s1 = s.replace("gasgg5","")
s2 = s1.replace("@#vscsd!s*","")
print(s2)