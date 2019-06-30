n = int(input("enter no of rows: " ))
for rows in range(1, n+1):
    for col in range (1, rows+1):
        print("*", end = "")
    print()
for rows in range(n-1,0,-1):
    for col in range(rows-1,0,-1):
        print("*" , end = "")
    print()