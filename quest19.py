#palidrome tester
a = input("enter text: ").lower()
reverse = a[::-1]
if a == reverse:
    print("enterd text",a," is palindrome")
else:
    print("enterd text",a," is not a palindrome")