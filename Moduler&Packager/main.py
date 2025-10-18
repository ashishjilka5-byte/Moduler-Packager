from package import datetime_ops,Mathematical_ops,random_ops,uuid_ops,File_ops,Explore_module,exit


def main_menu():
    while True:
        print("==========================================")
        print("Welcome to Multi-Utility Toolkit")
        print("==========================================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit\n")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            datetime_ops()
        elif choice == 2:
            mathematical_operations()
        elif choice == 3:
            random_data_generation()
        elif choice == 4:
            generate_uuid()
        elif choice == 5:
            file_operator()
        elif choice == 6:
            explore_module_attributes()
        elif choice == 7:
            exit_ops()




main_menu()
