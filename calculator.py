number1 = int(input("enter number1"))
operator = input("enter operator")
number2 = int(input("enter number2"))
if operator == "+":
    c=number1+number2
    print(c)
elif operator=="-":
    c=number1-number2
    print(c)
elif operator == "*":
    c=number1*number2
    print(c)
elif operator == "/":
    c=number1/number2
    print(c)
else:
    print("error")