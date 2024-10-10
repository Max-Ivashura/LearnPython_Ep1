email = input("Enter your email: ")

username = email[:email.find('@')]
domain = email[email.find('@')+1:]

print(f"Your username is {username} and domain is {domain}")