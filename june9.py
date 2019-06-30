# #print(list(range(1,10,2)))

# # n = int(input("enter rows: "))
# # for i in range(1,n):
# #     print("*"*i)

# a = 2
# b = a
# b = 5
# print(a)
# print(b)

# print("a", end = "" )
# print("a", end = "" )
# print("a", end = "" )
# print("a", end = "" )

# a = "ayesha"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())

#student = ["ayesha", 923408652122, "1998" ]

#dictionaries
student = {
    "name" : "ayesha",
    "cell#" : 923408652122,
    "age" : 21,
    "father name" : "jawed"
}
# print(student)
# print(student["name"])
# student["name"] = "ayesha jawed"
# print(student)
# student["module"] = "module 1"
# student["course"] = "artificial intelligence"
# print(student)
# del student["module"]
# print(student.pop("name"))
# print(student)

# students = []
# for i in range(3):
#     student = {}
#     student["name"] = input("enter name: ")
#     student["father name"] = input("enter father name: ")
#     student["age"] = input("enter age: ")
#     students.append(student)
# print("currently enrolled students" , len(students))
# for student in students:
#     print("student")
#     print(student)
#     print(students)
#     # if student["name"].lower() == "inam":
#     #     print("yes inam is our student")

print(student.values())
print(student.keys())
print(student.items())
# for k in student:
#     print(student[k])
#     print(k)

print("name" in student)