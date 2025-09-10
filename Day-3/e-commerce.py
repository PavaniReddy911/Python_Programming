cart=[]
def add_product(product):
    cart.append(product)
    print(product, "added to the cart.")

def remove_product(product):
    if product in cart:
        cart.remove(product)
        print(product, "removed from the cart.")
    else:
        print(product, "not found in the cart.")

def search_product(product):
    if product in cart:
        print(product, "is in the cart.")
    else:
        print(product, "not found in the cart.")

def display_cart():
    if not cart:
        print("Cart is empty.")
    else:
        print("Products in the cart:", cart)

def total_products():
    print("Total number of products in the cart:", len(cart))


while True:
    print("\n--- Cart Operations ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Display Cart")
    print("5. Show Total Products")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        prod = input("Enter product to add: ")
        add_product(prod)
    elif choice == 2:
        prod = input("Enter product to remove: ")
        remove_product(prod)
    elif choice == 3:
        prod = input("Enter product to search: ")
        search_product(prod)
    elif choice == 4:
        display_cart()
    elif choice == 5:
        total_products()
    elif choice == 6:
        print("Exiting... Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
