marks = {
    "Deven" : 100,
    "Aryan" : 56,
    "Sachin" : 23,
    0 : "Karan"
}

print(marks, type(marks))
print(marks["Deven"])
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Deven": 99, "Renuka" : 78}))
# print(marks.get("Deven1")) #prints none
# print(marks["Deven1"]) # returns an error
print(len(marks))