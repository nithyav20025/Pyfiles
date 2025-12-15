def outer(name):
    def inner():
        return f"Welcome to our home {name}"
    return inner

hello = outer("Vicky")
print(hello())
