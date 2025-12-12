def gmail_email(username, domain="gmail.com"):
    return f"{username}@{domain}.com"

def amazon(username, domain="amazon.com"):
    return f"{username}@{domain}.com"

def hotmail(username, domain="hotmail.com"):
    return f"{username}@{domain}.com"

def infosys(username, domain="infosys.com"):
    return f"{username}@infosys.com"

def build_email(username, email_func):
    return gmail_email(username)

print(build_email("vicky", "gmail.com"))
print(build_email("nithya", "amazon.com"))
print(build_email("nithu", "hotmail.com"))
print(build_email("vignesh", "infosys.com"))
