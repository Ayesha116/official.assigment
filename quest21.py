#write a python program to construct pattern
for i in range(1,6):
    for j in range(1,i):
        print("* ",end = "")
    print(" ")
for x in range(6,1,-1):
    for y in range(1,x):
        print("* ",end = "")
    print(" ")