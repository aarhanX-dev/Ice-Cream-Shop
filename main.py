flavours = {
    "chocolate": 1.0,
    "vanilla": 3.5,
    "strawberry": 1.5,
    "mango": 4.5
}

toppings = {
    "sprinkles": 1.0,
    "nuts": 1.5
}

ic = None

def menu():
    print(
        "<==MENU==>\n"
        "Chocolate: $1.0\n"
        "Vanilla: $3.5\n"
        "Strawberry: $1.5\n"
        "Mango: $4.5\n"
        "<==TOPPINGS==>\n"
        "Sprinkles: $1.0\n"
        "Nuts: $1.5"
    )

class IceCream:
    def buy_ice_cream(self, flavour, topping):
        self.flavour = flavour
        self.topping = topping

        if flavour in flavours:
            self.price = flavours[flavour]
        else:
            raise ValueError("Invalid Flavour!")

        if topping in toppings:
            self.priceT = toppings[topping]
            self.price += self.priceT
        elif topping == "none":
            print("Okay I won't set any topping!")
        else:
            raise ValueError("Invalid Topping!")

def get_info(temp):
    print(f"<==info==>\nFlavour: {ic.flavour}\nTopping: {ic.topping}\nBill: {ic.price}")

def message():
    print(
        "<==Options==>\n"
        "1) Add to cart\n"
        "2) Buy ice cream\n"
        "3) Cart\n"
        "4) Exit"
    )

message()

while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        menu()
        flavour = input("Enter flavour: ").lower().strip()
        topping = input('Enter topping (tip: write "none" for no topping): ').lower().strip()
        ic = IceCream()
        ic.buy_ice_cream(flavour, topping)
        message()

    elif choice == 2:
        if ic is None:
            print('No items in the cart. Type "1" to add something in your cart!')
            message()
        else:
            print(f"Thanks for purchasing! Have a good day!\nBill: {ic.price}")
            break

    elif choice == 3:
        if ic is None:
            print("Can't show info until you add something to the cart!")
            message()
        else:
            get_info(ic)
            message()

    elif choice == 4:
        print("Thanks for visiting! Have a nice day.")
        break

    else:
        print("Invalid choice!")
        message()

print("<==END OF PROGRAM==>")
