def press(callback):
    print("Press enter to continue...")
    callback()

def show_msg():
    print("Hello Vicky Welcome to our website")

press(show_msg)