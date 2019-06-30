#Write a program to convert binary number to Decimal number
num = int(input("Enter binary number: "))
a = 0
i = 0
#print("decimal representation of ",n,end=" is ")
while (n!=0):
    rem =int(n%10)
    a =a+rem*(2**i)
    n = n/10
    i+=1
print(a)
