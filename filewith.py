
# # read file

# f = open("dev.txt")
# data = f.read()
# print(data)
# f.close()


# # write file

# st = "hey deven you are amazing"
# f = open("dev.txt", "w")
# f.write(st)
# f.close()



# # read lines of file

# f = open("myfile.txt")

# lines = f.readlines()
# print(lines, type(lines))

# f.close()





# # with stmt

# f = open("dev.txt")
# print(f.read())
# f.close()

# # the same can be written using with statement like this:
# with open("dev.txt") as f:
#     print(f.read())

# # you dont have to explicitly close the file