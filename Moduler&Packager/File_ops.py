import os


def file_operator():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            filename = input("Enter file name: ")
            open(filename, "w").close()
            print("File created successfully!")
            print("===============================================")


        elif choice == 2:
            filename = input("Enter file name: ")
            if not os.path.exists(filename):
                print("File not found! Please create the file first.")
            else:
                data = input("Enter data to write: ")
                with open(filename, "w") as f:
                    f.write(data)
                print("Data written successfully!")
                print("===============================================")

        elif choice == 3:
            filename = input("Enter file name: ")
            with open(filename, "r") as f:
                print("File Content:")
                print(f.read())
                print(f.close())
                print("===============================================")

        elif choice == 4:
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            with open(filename, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully!")
            print("===============================================")

        elif choice == 5:
            print("Back to main menu")
            break

        else:
            print("Invalid choice! Try again.")
