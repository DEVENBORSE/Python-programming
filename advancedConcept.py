
# # using walrus operator

# if(n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"list is too long ({n} elements, expected <=3)") # output : list is too long (5 elemnts, expected <3)


# # type definitions:

# n : int = 5
# name : str = "Deven"

# def sum(a, b) -> int:
#     return a+b


# # importing for type definitions

# from typing import List, Union, Tuple, Dict

# numbers: List[int] = [1,2,3,4,5]

# person: Tuple[str, int] = ("Deven", 89)

# scores: Dict[str, int]= {"Deven": 89, "Aryan": 90}

# identifier: Union[int, str] = "ID123"
# identifier = 12345 # also valid



# # match case

# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server error"
#         case _:
#             return "Unknown status"

# print(http_status(200))
# print(http_status(404))
# print(http_status(500))




# # dictionary merge and update operations

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = dict1 | dict2
# print(merged)





 
# # enumerate func  : The 'enumerate' function adds counter to an iterable and return it

# l = [3, 513, 53, 535]

# for index, item in enumerate(l):
#     print(f"the item number at index {index} is {item}")




# # MAP ex

# l = [1, 2, 3, 4, 5]

# square = lambda x:x*x

# sqlist = map(square, l)
# print(list(sqlist))




# # Filter Ex

# def even(n):
#     if(n%2 == 0):
#         return True
#     return False


# onlyEven = filter(even, l)
# print(list(onlyEven))



# # reduce func

# from functools import reduce

# def sum(a, b):
#     return a + b
# print(reduce(sum, l))



