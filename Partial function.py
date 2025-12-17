def calculate_price(base_price, tax_price):
    return base_price * (1 + tax_price)

print(calculate_price(100, 20))
print(calculate_price(230, 40))

from functools import partial

def calculate_price(base_price, tax_price):
    return base_price * (1 + tax_price)

price_with_gst = partial(calculate_price, tax_price=2)


print(price_with_gst(1000))
print(price_with_gst(500))
