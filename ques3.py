a = int(input("Enter numerator: "))
b = int(input("enter denominator: "))
if a%b==0:
    print("Number ",a,"is completely divisible by number", b)
elif a%b!=0:
    print("Number ",a,"is not completely divisible by number", b)