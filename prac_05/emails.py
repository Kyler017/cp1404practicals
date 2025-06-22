def main():
    email_of_name = {}
    email = input("please enter Email: ")
    while email != " ":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != " ":
            name = input("please enter Name: ")
        email_of_name[email] = name
        email = input("please enter Email: ")

    for email, name in email_of_name.items():
        print(f"{name} {email}")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " "
    return name