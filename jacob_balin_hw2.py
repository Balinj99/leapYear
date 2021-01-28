def main():
    running = True
    while(running):
        try:
            year = int(input("\nPlease enter a year: "))

        except:
            print("\nIncorrect input. Please try again.")
            continue

        else: 
            if(year %4 == 0 and year % 100 != 0):
                print("The year ", year, " is a leap year.")

            elif(year % 400 == 0 and year % 100 == 0):
                print("The year ", year, " is a leap year.")

            else:
                print("The year ", year, " is not a leap year.")
       
        running2 = True
        while(running2):
            keepGoing = input("\nEnter another year? y/n: ")

            if(keepGoing == "y"):
                running2 = False

            elif(keepGoing == "n"):
                print("\nGoodbye!\n")
                running2 = False
                running = False

            else:
                print("Incorrect input. Please try again.")

if __name__ == "__main__":
    main()