import random
import string


def random_data_generation():
    while True:
        print("\nRandom Data Generation: ")
        print("1. Generation Random number ")
        print("2. Generation Random list ")
        print("3. Create Random Password")
        print("4. Generation Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            start = int(input("Enter start value: "))
            end = int(input("Enter end value: "))
            print(f"Random Number: {random.randint(start, end)}")

        elif choice == 2:
            n = int(input("How many random numbers you want in list? "))
            start = int(input("Enter start value: "))
            end = int(input("Enter end value: "))
            rand_list = [random.randint(start, end) for _ in range(n)]
            print("Generated Random List:", rand_list)

        elif choice == 3:
            length = int(input("Enter password length: "))
            all_chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(all_chars) for _ in range(length))
            print("Generated Password:", password)

        elif choice == 4:
            digits = "0123456789"
            otp = ''.join(random.choice(digits) for _ in range(6))
            print("Generated OTP:", otp)

        elif choice == 5:
            print("Back to Main Menu")
            break

        else:
            print("Invalid choice! Try again.")
