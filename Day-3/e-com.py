cart = []

def add(product):
    cart.append(product)
    print(product, "added to the cart.")

def remove(product):
    if product in cart:
        cart.remove(product)
        print(product, "removed from the cart.")
    else:
        print("Product not found in the cart.")

def search(product):
    if product in cart:
        print(product, "is there in the cart.")
    else:
        print(product, "is not in the cart.")

def display():
    if not cart:
        print("Cart is empty.")
    else:
        print("Products in the cart:", cart)

def total():
    print("Total number of products in the cart:", len(cart))

def sort_cart():
    if not cart:
        print("Cart is empty. Cannot sort.")
    else:
        cart.sort()
        print("Cart sorted:", cart)

def clear_cart():
    cart.clear()
    print("Cart cleared successfully.")

while True:
    print("\nCart Operations")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Display Cart")
    print("5. Show Total Products")
    print("6. Sort Cart")
    print("7. Clear Cart")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        prod = input("Enter product to add: ")
        add(prod)
    elif choice == 2:
        prod = input("Enter product to remove: ")
        remove(prod)
    elif choice == 3:
        prod = input("Enter product to search: ")
        search(prod)
    elif choice == 4:
        display()
    elif choice == 5:
        total()
    elif choice == 6:
        sort_cart()
    elif choice == 7:
        clear_cart()
    elif choice == 8:
        print("Exiting... Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
