import math

def mathematical_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter a Number: "))
            print(f"Factorial: {math.factorial(n)}")
            print("===============================================")

        elif choice == 2:
            x = float(input("\nEnter principal amount: "))
            y = float(input("Enter rate of interest (in %): "))
            z = float(input("Enter time (in years): "))
            amount = x * (pow((1 + y / 100), z))
            print(f"Compound Interest: {round(amount,2)}")
            print("===============================================")

        elif choice == 3:
            angle = math.radians(float(input("Enter angle in degrees: ")))
            print(f"sin({math.degrees(angle)}) = {math.sin(angle):.4f}")
            print(f"cos({math.degrees(angle)}) = {math.cos(angle):.4f}")
            print(f"tan({math.degrees(angle)}) = {math.tan(angle):.4f}")
            print("===============================================")

        elif choice == 4:
            print("1. Area of Circle")
            print("2. Area of Rectangle")
            print("3. Area of Triangle")
            print("4. Area of Square")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                r = float(input("Enter radius: "))
                print(f"Area of Circle: {math.pi * r * r:.2f}")

            elif sub_choice == 2:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                print(f"Area of Rectangle: {l * b:.2f}")

            elif sub_choice == 3:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"Area of Triangle: {0.5 * base * height:.2f}")

            elif sub_choice == 4:
                s = float(input("Enter side: "))
                area = s ** 2
                print("Area of Square =", round(area, 2))

            else:
                print("Invalid choice!")

        elif choice == 5:
            print("Back to Main Menu")
            break

        else:
            print("Invalid choice! Try again.")
