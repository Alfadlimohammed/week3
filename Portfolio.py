user_name = input("Enter your name: ")
if user_name:
    print(f"Hello, {user_name}!")
else:
    print("Hello, Stranger!")
if __name__ == '__main__':
    password1 = input("Enter a new password: ")
    password2 = input("Enter the password again: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")
if __name__ == '__main__':
    password1 = input("Enter a new password (8-12 characters): ")
    if 8 <= len(password1) <= 12:
        password2 = input("Enter the password again: ")
        if password1 == password2:
            print("Password Set")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Password must be between 8 and 12 characters long.")
if __name__ == '__main__':
    # Define the list of common passwords
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

    # Prompt the user to enter a new password
    password1 = input("Enter a new password (8-12 characters): ")

    # Check if the password meets the length requirement
    if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        password2 = input("Enter the password again: ")
        if password1 == password2:
            print("Password Set")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Please choose a password between 8 and 12 characters that is not too common.")
if __name__ == '__main__':
       while True:
            password = input("Enter a password: ")
            if len(password) >= 6:
                print("You have successfully chosen a password:", password)
                break
            else:
                print("Password must be at least 6 characters long. Please try again.")
if __name__ == '__main__':
    for i in range(13):
        result = i * 7
        print(f"{i} x 7 = {result}")
if __name__ == '__main__':
    table_number = int(input("Enter a number (0 to 12) for the times table: "))

    if 0 <= table_number <= 12:
        for i in range(13):
            print(i, "x", table_number, "=", i * table_number)
    else:
        print("Please enter a number between 0 and 12.")
if __name__ == '__main__':
    table_number = int(input("Enter the number for the times table (-12 to 12): "))
if -12 <= table_number <= 12:
    if table_number < 0:
        for i in range(12, -1, -1):
            print(f"{i} x {abs(table_number)} = {i * table_number}")
    else:
        for i in range(13):
            print(f"{i} x {table_number} = {i * table_number}")
else:
    print("Please enter a number between -12 and 12.")