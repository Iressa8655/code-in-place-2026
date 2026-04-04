""""
IDE | Dog yearsDownload Project

Left column expanded containing null
Assignment
Write a program which asks a user to input an age in human years, and converts it to the equivalent age in dog years.




Dogs have different lifespans than humans. Thus there age is sometimes reported in "dog years" which are scaled to be comparable to human ages. On average every calendar year is equal to 7.18 dog years. To convert 3 calendar years to dog years, you multiply 3 * 7.18 to get 21.54 dog years. That means, if your dog is 3 years old, they're past their teenage years!



Your program will take in an age in calendar years, multiply that age by 7.18 and report the resulting dog years. Here's a sample run of the program (user input is in blue):

Enter an age in calendar years: 10
That's 71.8 in dog years!"""
# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    pass  # Delete this line and write your code here! :)
    human_years=input("Enter an age in calendar years: ")
    human_years=float(human_years)*7.18
    print("That's", human_years, "in dog years" , "!")
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()