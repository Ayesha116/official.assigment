#count alphabet,numbers and special charcters,spaces
word = input("enter word: ").lower()
alphabet = 0
space = 0
number = 0
special_characters = 0
for i in word:
    if i=="a"or i =="e" or i == "o" or i == "u" or i == "i" or  i =="b" or i =="c" or i =="d" or i =="f" or i =="g" or i =="h" or i =="j" or i =="k" or i =="l" or i =="m" or i =="n" or i =="p" or i =="q" or i =="r" or i =="s" or i =="t" or i =="v" or i =="w" or i =="x" or i =="y" or i =="z":
        alphabet = alphabet+1
    elif i == " ":
        space = space+1
    elif i == "1" or i == "2" or i == "3" or i =="4" or i =="5" or i == "6" or i =="7" or i =="8" or i == "9" or i =="0":
        number = number +1
    elif i == "=" or i == "'" or i == ";" or i == ":" or i == "|" or i == "!" or i == "*" or i == "^" or i == "$" or i == "%" or i == "#" or i == "@" or i == "<" or i == ">" or i == ".": 
        special_characters = special_characters+1
print("alphabets =",alphabet)
print("spaces=",space)
print("number=",number)
print("special charcters = ",special_characters)