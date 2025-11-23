#L - Local variable

def order():
    food="Fried Rice"
    print("Your order is:", food)

order()

#E - Enclosing

def amount():
    discount = 100

    def price():
        print("net amount:", discount)

    price()


amount()
#G - Global variable

school_name= "SHC"
number_of_students= 3000
def profile():
    print("School name is:", school_name)

def students():
    print("Number of students:", number_of_students, school_name)

profile()
students()



ecommerce_platform="amazon"

def category():
    product="Home appliance"
    def name():
        item="Television"
        def price():
            item_price= 49000
            def net_quantity():
                quantity= 2
                print(f"Order placed: {product} {item} {item_price} {quantity} using {ecommerce_platform}")
            net_quantity()

        price()

    name()


category()


