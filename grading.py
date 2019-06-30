print(input("enter your name "))
a = int(input("Enter your physics marks "))
b = int(input("Enter your mathematics marks "))
c = int(input("Enter your english marks "))
d = int(input("Enter your chemistry marks "))
e = int(input("Enter your urdu marks "))
Total_marks = a + b + c + d + e
percentage = (Total_marks/500)*100
if percentage >=80:
    print("your percentage is " + str(percentage)+" and Grade is A+")
elif percentage >=70:
    print("your percentage is " + str(percentage)+" and Grade is A")
elif percentage>=60:
    print("your percentage is " + str(percentage)+" and Grade is B")
elif percentage >=50:
    print("your percentage is " + str(percentage)+" and Grade is C")
elif percentage>=40:
    print("your percentage is " + str(percentage)+" and Grade is D")
else:
    print("your percentage is " + str(percentage)+" and you are fail")