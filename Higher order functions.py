def build_email(username, provider):
    if provider == 'gmail':
        return f"{username}@gmail.com"
    elif provider == 'yahoo':
        return f"{username}@yahoo.com"
    elif provider == 'accenture':
        return f"{username}@accenture.com"
    elif provider == 'infosys':
        return f"{username}@infosys.com"
    elif provider == 'amazon':
        return f"{username}@amazon.com"
    elif provider == 'hotmail':
        return f"{username}@hotmail.com"
    else:
        return "Unknown provider"

print(build_email('vicky', 'gmail'))
print(build_email('nithu', 'yahoo'))
print(build_email('sanjay', 'accenture'))
print(build_email('nivyan', 'infosys'))
print(build_email('sree', 'amazon'))
print(build_email('surya', 'hotmail'))
