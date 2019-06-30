import datetime
v = input("If you want to continue...Yes...\notherwise press any key to exit : ")
print(" ")
while True:
	a = input(":>>")
	if a == "exit" or  a == "no":
		break
	elif a == "date":
		print(datetime.date.today())
	elif a == "name" or a == "your name" or a == "what is your name" or a == "what is your good name":
		print("Osama robot".title())
	elif a == "time":
		print(datetime.datetime.now())
	elif a == "gender" or a == "your gender":
		print("Sorry! no gender")
	elif a == "what are you doing" or a == "what are you doing now":
		print("Answering to you")
	elif a == "bye" or a == "byee":
		print("Allah hafiz")
	else:
		print(">>"+" "+a.title()+" "+ "\nsyntax error :")
		print(" ")