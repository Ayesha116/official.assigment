# # a = int(input("enter number1: "))
# # b = int(input("enter number2: "))
# # def sub(num1,num2):
# #     c = num1 - num2
# #     print(c)
# # def mult(num1,num2):
# #     mul= num1 * num2
# #     print(mul)
# # def div(num1,num2):
# #     divi= num2/num1
# #     print(divi)
# # sub(a,b)
# # mult(a,b)
# # div(a,b)


# # position
# def my_pet(owner, pet):
#     print(owner, "is an owner of ", pet)
# my_pet("cat","Sarah")
# # keyword argument passing
# def my_pet(owner, pet):
#     print(owner, "is an owner of ", pet)
# my_pet(pet="cat",owner="Sarah")

# # default parameter
# def my_pet(owner, pet,city=karachi):#karachi default me dia hua h agr mny neechy argument me pass nh kri tw yh karachi print krdega.. lkn agr defalut nh di hui tw phir parameter pass krna zaruri h
#     print(owner, "is an owner of ", pet,".They are from",city)
# my_pet(pet="cat",owner="Sarah")#yhn city ka parameter hmny nh pass kia tw wo default me karachi print kr dega.. lkjn agr yhn mny city dia kuch or tw wo wahi print krega

# #takes nothing and return something
# def sum():
#     a=2
#     b=3
#     return(a+b)
# result=sum()
# print(result)

# #takes something and returns something
# def sum(val1,val2):
#     result=val1+val2
#     return result
# output_of_result= sum(a.b)
# print(output_of_result)


#task:
#take an input from user , pass it in the argument and return whether it is even or odd
a=int(input('Enter Any Num'))
def even(num):
    if num % 2 == 0:
        return 'Num is Even'
    else:
        return 'Num is Odd'
output=even(a)
