import csv

total_amount = 0

mydict = []


def addAmount(amount):
    global total_amount
    total_amount += amount


def product_details(choice):
    if choice == 1:
        print("You chose to buy Trousers\nAvailable sizes --->\n")
        size = size_guide()
        print("\nCost of trouser = 1500/-")
        cart = int(input('1 - ADD TO CART, 0 - GO BACK : '))
        if cart:
            quan = int(input('Enter quantity '))
            print("You are buying", quan, size, "sized trousers")
            addAmount(quan * 1500)
            mydict.append(
                {'Product Name': 'Trousers', 'Quantity Purchased': quan, 'MRP': 1500, 'Total Amount': quan * 1500})
            display_products()
        else:
            display_products()

    elif choice == 2:
        print("You chose to buy Shirt\nAvailable sizes --->\n")
        size = size_guide()
        print("\nCost of Shirt = 1000/-")
        cart = int(input('1 - ADD TO CART, 0 - GO BACK : '))
        if cart:
            quan = int(input('Enter quantity '))
            print("You are buying", quan, size, "sized Shirt")
            addAmount(quan * 1000)
            mydict.append(
                {'Product Name': 'Shirt', 'Quantity Purchased': quan, 'MRP': 1500, 'Total Amount': quan * 1000})
            display_products()
        else:
            display_products()

    elif choice == 3:
        print("You chose to buy T-Shirt\nAvailable sizes --->\n")
        size = size_guide()
        print("\nCost of T-Shirt = 700/-")
        cart = int(input('1 - ADD TO CART, 0 - GO BACK : '))
        if cart:
            quan = int(input('Enter quantity '))
            print("You are buying", quan, size, "sized T-Shirt")
            addAmount(quan * 700)
            mydict.append(
                {'Product Name': 'T-Shirt', 'Quantity Purchased': quan, 'MRP': 700, 'Total Amount': quan * 700})
            display_products()
        else:
            display_products()

    elif choice == 4:
        print("You chose to buy Jeans\nAvailable sizes --->\n")
        size = size_guide()
        print("\nCost of Jeans = 1200/-")
        cart = int(input('1 - ADD TO CART, 0 - GO BACK : '))
        if cart:
            quan = int(input('Enter quantity '))
            print("You are buying", quan, size, "sized Jeans")
            addAmount(quan * 1200)
            mydict.append(
                {'Product Name': 'Jeans', 'Quantity Purchased': quan, 'MRP': 1200, 'Total Amount': quan * 1200})
            display_products()
        else:
            display_products()

    elif choice == 5:
        print("You chose to buy Kurtas\nAvailable sizes --->\n")
        size = size_guide()
        print("\nCost of Kurtas = 500/-")
        cart = int(input('1 - ADD TO CART, 0 - GO BACK : '))
        if cart:
            quan = int(input('Enter quantity '))
            print("You are buying", quan, size, "sized Kurtas")
            addAmount(quan * 500)
            mydict.append(
                {'Product Name': 'Kurtas', 'Quantity Purchased': quan, 'MRP': 500, 'Total Amount': quan * 500})
            display_products()
        else:
            display_products()

    else:
        print("\nTotal Amount = ", total_amount)
        print('\nThank You for your Purchase\nA payment link will be shared to your registered mobile number '
              'soon!! \nHope to see you back soon!!')


def size_guide():
    print("S  ---  C:32 W:34 S:18\nM  ---  C:34 W:36 S:20\nL  ---  C:36 W:38 S:22")
    size = int(input('Choose size 1-3 : '))

    if size == 1:
        return "S"
    elif size == 2:
        return "M"
    else:
        return "L"


def display_products():
    print("1.Trousers\n2.Shirt\n3.T-Shirt\n4.Jeans\n5.Kurtas\n6.CheckOut")
    choice = int(input('choose what you wanna buy : '))
    product_details(choice)


fields = ['Product Name', 'Quantity Purchased', 'MRP', 'Total Amount']


def add_to_order():
    filename = 'checkout.csv'
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names) 
        writer.writeheader()

        # writing data rows 
        writer.writerows(mydict)


display_products()
add_to_order()

