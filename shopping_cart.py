class Product():
    def __init__(self):
        self.products = {
                "001" : {
                    "name" : "Fresh milk",
                    "price": 15.00,
                    "stock": 10,
                    "category": "drinks"
                },
                "002" : {
                    "name" : "Nutri Malt",
                    "price": 8.80,
                    "stock": 3,
                    "category": "drinks"
                },
                "003" : {
                    "name" : "Coca Cola",
                    "price": 3.00,
                    "stock": 15,
                    "category": "drinks"
                },
                "101" : {
                    "name" : "Shin ramen",
                    "price": 22.00,
                    "stock": 20,
                    "category": "food"
                },
                "102" : {
                    "name" : "Maggi Kari",
                    "price": 5.00,
                    "stock": 25,
                    "category": "food"
                },
                "103" : {
                    "name" : "Indomee",
                    "price": 7.50,
                    "stock": 15,
                    "category": "food"
                },

                "201" : {
                    "name" : "Chipsmore",
                    "price": 7.00,
                    "stock": 0,
                    "category": "food"
                },
                "202" : {
                    "name" : "Tigers",
                    "price": 2.50,
                    "stock": 3,
                    "category": "food"
                },
                "203" : {
                    "name" : "Oat Krunch",
                    "price": 14.00,
                    "stock": 11,
                    "category": "food"
                }
            }
        
    def display_product(self):
        for number, details in self.products.items():
            print(f"{number} - {details['name']} - Price: RM{details['price']}")


product = Product()


class ShoppingCart():

    def __init__ (self):
        self.shopping_cart = []

    def check_stock(self, item_num, quantity):
    # use the input (item num) to access he dict to check the stock 
        stock = product.products[item_num]["stock"]
        # compare the quantity with the stock):
        if stock == 0:
            print("There are currently no stock for", product.products[item_num]['name'], "\n")
            return False
        elif quantity >  stock:
            print("There are only", stock, "stock for", product.products[item_num]['name'], "\n")
            return False
        else:
            print(quantity, product.products[item_num]['name'], "has been added to your cart\n")
            product.products[item_num]["stock"] -= quantity
            return True
        

    def add_item(self, item_num, quantity):
        tempList = [item_num, quantity]
        self.shopping_cart.append(tempList)


    def calculate_total(self, quantity):
        total = 0
        for sublist in self.shopping_cart:
            item_num = sublist[0]
            item_price = product.products[item_num]["price"]
            total += item_price * quantity
        return total
            


    def checkout(self, quantity):
        total = self.calculate_total(quantity)
        print('\n---------------------------------------')
        print('                RECEIPT        ')
        print('---------------------------------------')
        for sublist in self.shopping_cart:
            item_num = sublist[0]
            quantity = sublist[1]
            item_desc = product.products[item_num]["name"]
            item_price = product.products[item_num]["price"]
            total += item_price * quantity
            print(str(quantity)+"x", str(item_desc),"       ", "RM"+str(item_price))
        print("Your Total is:", total)
        print('Thank you very much!')




def print_options():
    print("\nEnter a number to proceed")
    print("1 - Display Catalogue")
    print("2 - Place item in cart")
    print("3 - quit\n")



cart = ShoppingCart()
print("Welcome...")
print_options()
option = input("Enter a number (3 to quit):")

break_to_2 = False
break_all = False

while option != "3":
    if option == "1":
        product.display_product()
    elif option == "2":
        while True:
            item_num = input('Enter item number:')
            if item_num in product.products.keys():
                try:
                    quantity = int(input("Enter quantity:"))
                    if cart.check_stock(item_num, quantity) == True:
                        cart.add_item(item_num, quantity)

                        checkout = input("Ready to checkout? (Y/N)\n").lower()
                        while True:
                            if checkout == "y":
                                cart.checkout(quantity)
                                break_to_2 = True
                                break
                            elif checkout == "n":
                                break_all = True
                                break
                            else:
                                print("Please answer a yes or no")
                                checkout = input("Ready to checkout? (Y/N)\n").lower()
                except:
                    print("Not a quantity.")
        
            else:
                print("Item is not found!")
            if break_to_2:
                break
        if break_all:
            break

            
    else:
        print('Not a valid input(stop trolling!)')

    print_options()
    option = input("Enter a number (3 to quit):")

