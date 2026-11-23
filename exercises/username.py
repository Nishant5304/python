
username = input("Enter your username: ")

if len(username) > 12:
    print("username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("username can't have any spaces")
elif not username.isalpha():
    print("username can't be digits")
else:
    print(f"Welcome, {username}")