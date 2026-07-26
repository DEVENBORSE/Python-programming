# a = [ 1,2,3,4,5,6,7,8,9]
# print(a[::2])

# a = [1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a = [ 1,2,3,4,5]
# print(a[3:0:-1])

# def func(value, values):
#     value = 1
#     values[0]=44
#     t = 3
#     v = [1,2,3]
#func(t,v)
#print(t,v[0])

# arr = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop(),end=" ")


# def f(i,values=[]):
#     values.append (i)
#     print(values)
#     return values
# f(1)
# f(2)
# f(3)


# arr = [1,2,3,4,5,6]
# for i in range(0,6):
#     arr[i]= arr[i]-1
# print(arr[i],end = " ")


# fruit_list1 = [ 'Apple' ,'Berry' ,'Cherry' ,'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#     sum +=1

# if ls[1] == 'Kiwi':
# sum += 20

# print(sum)


# for i , j in zip(range(1,6),range(5,0,-1)):
#         if i == 3 and j == 3:
#             continue
#         print(i," ",j)


# fruit = {}
# def addone(index):
#     if index in fruit :
#         fruit[index] +=1
#     else:
#         fruit[index] = 1 
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))            

# arr = {}
# arr[1]= 1
# arr['1']=2
# arr[1]+= 1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)    

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)    

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# sum += my_dict[k]
# print(sum)
# print(my_dict)    

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['box'] = jars
# print(len(crates[box]))

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print (dict[_],end = " ")


# math = 50
# chem = 60
# print(id(math))
# print(id(chem))

# rec = {"Name":"python","Age":20}
# r = rec.copy()
# # print(id(r)==id(rec))
# print(id(r))
# print(id(rec))

# rec = {"Name":"python","Age":"20","Addr":"Nj","Country" : "USA"}
# id1 = id(rec)
# del rec
# rec = {"Name":"python","Age":"20","Addr":"Nj","Country" : "USA"}
# id2 = id(rec)
# print(id1==id2)

# val = [0,1,0,3,12]
# for i in val :
#     if i == 0:
#         val.remove(i)
#         val.append(i)
# print(val)        

# arr1 = [1,2,3]
# arr2 = [2,3,4]
# arr3 = [3,4,5]
# for i in arr1:
#     if i in arr2 and i in arr3:
#         print(i,end = " ")


# arr4 = [1,2,11,1,3,1,1,1,1,1,1,1,1,1,1]  #maximum consective 1's
# count = 0
# max_count = 0
# for i in arr4:
#     if i == 1:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)

#palindrome check
# arr1 = [1,2,3,2,1]
# is_palindrome = True
# for i in range(len(arr1) // 2):
#     if arr1[i] != arr1[len(arr1) - 1 - i]: # len(arr1) - 1 - i : gives the index of the element from the end
#         is_palindrome = False
#         break

# print(is_palindrome)


#another way to check palindrome
# arr2 = [1,2,3,2,1]
# if arr2[:] == arr2[::-1]: # arr2[::-1] : gives the reversed array
#     print("Palindrome")
# else :
#     print("Not a Palindrome")


# reverse a string
# str1 = "hello"
# str2 = str1[::-1]
# print(str2)

# # string palindrome check
# str3 = "racecar"
# if str3[:] == str3[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# # using loop palindrome check
# str4 = "hello"
# is_palindrome = True
# for i in range(len(str4) // 2):
#     if str4[i] != str4[len(str4) - 1 - i]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# # using loop to reverse a string
# str5 = "hello"
# str6 = ""
# for i in range(len(str5) - 1, -1, -1):
#     str6 += str5[i]
# print(str6)

#removing duplicate characters from a string
# str7 = "programming"
# str8 = ""
# for char in str7:
#     if char not in str8:
#         str8 += char
# print(str8)

def findTotaldistance(n,arr):
    total = 0
    for i in range(n):
        total += abs(arr[i]-arr[i-1])
    return total
arr  = [10,11,7,12]
n = len(arr)
print(findTotaldistance(n, arr))