def main():
    running = True
    while(running):
        year = int(input("\nPlease enter a year: "))
                 
        if(year %4 == 0 and year % 100 != 0):
            print("The year ", year, " is a leap year.")

        elif(year % 400 == 0 and year % 100 == 0):
            print("The year ", year, " is a leap year.")

        else:
            print("The year ", year, " is not a leap year.")
            
        keepGoing = input("\nEnter another year? y/n: ")

        if(keepGoing == "n"):
            print("\nGoodbye!\n")
            running = False

if __name__ == "__main__":
    main()