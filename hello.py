cart = []
def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart.append([item, price])
    print("Item added successfully!\n")

def show_cart():
    if len(cart)==0:
        print("cart is Enpty.\n")
        return
    print("\n---Shopping Cart---")
    for item in cart:
        print(item[0], "-","$", item[1])
        print()
def culculate_total():
    total=0
    for item in cart:
        total+=item[1]
    print("Total Bill: $. ", total)
    print()
while True:
    print("====Grocery Billing system====")
    print("1.AddItem")
    print("2. Show Cart")
    print("3. Culculate total")
    print("4. Exit")

    choice = input("Enter Choice: ")
    if choice=="1":
        add_item()
    elif choice =="2":
        show_cart()
    elif choice =="3":
        culculate_total()
    elif choice =="4":
        print("Thank you for shopping")
        break
    else:
        print("invalid choice!\n")
