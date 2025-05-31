MINIMUM_LENGTH = 6
MAXIMUM_LENGTH = 10
password = input("Enter password(more than 6 numbers and less than 10 numbers):")
length = len(password)
while length < MINIMUM_LENGTH or length > MAXIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter your password(more than 6 numbers and less than 10 numbers):")
        length = len(password)
print("*" * length)
