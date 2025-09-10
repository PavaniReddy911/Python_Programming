def apply_discount(price, discount_percent):
    discount_amount = (discount_percent / 100) * price
    return price - discount_amount

def add_gst(price, gst_percent=18):
    gst_amount = (gst_percent / 100) * price
    return price + gst_amount

def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print("INVOICE")
    subtotal = 0

    for product, price in cart.items():
        print(f"{product:<15} : ${price}")
        subtotal += price

    print(f"Subtotal: ${subtotal}")

    if discount_percent > 0:
        discounted_price = apply_discount(subtotal, discount_percent)
        print(f"After {discount_percent}% discount: ${discounted_price}")
    else:
        discounted_price = subtotal

    final_price = add_gst(discounted_price, gst_percent)
    print(f"After {gst_percent}% GST: ${final_price:.2f}")
    print("Thank you for shopping with us!")
