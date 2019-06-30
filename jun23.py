# topic: variable scoping

# a = 2
# def my_func():
#     a = 9
#     print(a)
# my_func()
# print(a)

#topic: inner functions

# def calculate_taxes(percent):
#     def actual_tax(salary):
#         return salary*percent
#     return actual_tax


# actual_tax_fn = calculate_taxes(0.30)
# print(actual_tax_fn)
# print(actual_tax_fn(1000))


# def calculator(num1,num2,op)
#     def add(n1,n2):
#         return

# while loop
# import random
# temp = random.randint(10,47)
# while temp<45:
#     print("it\'s better weather" , temp)
#     temp = random.randint(30,50)
# print("i came back due to hot weather, temp=", temp)


# #class
# class Human():
#     def __init__(self): #pythons interpreter call it. you dont call it
#         print("i am a constructor")
# Human()
# Human()


# 
class Human():
    def __init__(self , name = "john doe", favrt_dish= "biryani"): 
        self.name = name
        print("i am a constructor")

    def set_age(self, favrt_dish):
        self.favrt_dish = favrt_dish


h1 = Human()
h2 = Human("biryani","Ayesha")
h3 = Human()
print(h2.name
print(h1.favrt_dish)]

