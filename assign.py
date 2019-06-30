products = [{'name':'clothes', 'quantity':1}]
while True:
    print("press 1 to sale item ")
    print("press 2 to puchase item")
    print("press 3 to delete product")
    print("press 4 to edit the data")
    print("press 5 to exit")
    choice = int(input("enter your choice"))
    if choice ==1:
        print(products)
    elif choice ==5:
        break