def email_builder(domain):
    def build_email(email):
        return f"{email}@{domain}"
    return build_email


gmail = email_builder("gmail.com")
ymail = email_builder("yahoo.com")
hotmail = email_builder("hotmail.com")

print(gmail("Vicky"))
print(ymail("Nithya"))
print(hotmail("Nivi"))