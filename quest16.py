#Write a Python program to calculate the sum of the digits in an integer
def decimaltobinary(num):
    if num>1:
        decimaltobinary(num//2)
    print(num%2)
a = int(input("enter number: "))
decimaltobinary(a)