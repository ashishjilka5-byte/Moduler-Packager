import datetime
import time


def datetime_menu():
    while True:
        print("Datetime and Time Operations:\n")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Mian Menu ")

        ch = int(input("\nEnter your choice:"))

        if  ch  == 1:
            now = datetime.datetime.now()
            print("\nCurrent Date and Time:", now.strftime("%y-%m-%d %H:%M:%S"))
            print("===============================================")

        elif  ch  == 2:
            day1 = input("Enter first date (YYYY-MM-DD): ")
            day2 = input("Enter second date (YYYY-MM-DD): ")
            date1 = datetime.datetime.strptime(day1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(day2, "%Y-%m-%d")
            diff = abs((date2 - date1).days)
            print("Difference:", diff, "days")
            print("===============================================")

        elif  ch  == 3:
            n = datetime.datetime.now()
            print("Custom format:", n)
            print("DD-MM-YYYY", n.strftime("%d-%m-%Y"))
            print("Full date and time: ", n.strftime("%A, %B %d, %Y %I:%M %p"))
            print("===============================================")

        elif  ch  == 4:
            print("Press Enter to start the stopwatch")
            input()
            start = time.time()
            print("Stopwatch started...")
            print("Press Enter to stop")
            input()
            end = time.time()
            print("Elapsed Time:", round(end - start, 2), "seconds")
            print("===============================================")

        elif  ch  == 5:
            seconds = int(input("Countdown Timer: "))
            while seconds > 0:
                print(seconds)
                time.sleep(1)
                seconds -= 1
            print("Time’s up!")
            print(" ")
            print("===============================================")

        elif  ch  == 6:
            print("Back to  Main Menu")
            break

        else:
            print("Invalid choice!")
