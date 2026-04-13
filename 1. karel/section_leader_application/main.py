"""
Mars Weight prompt

The problem you are to teach in the demo is Mars Weight. Here is the prompt that is given to the student:

An earthling's weight on Mars is 37.8% of their weight on earth. Write a Python program that prompts the user (an earthling) to enter their weight on earth and prints their calculated weight on Mars."""

MARS_MULTIPLE=0.378
def main():
    earth_weight_str=input("Enter a weight on earth: ")
    #turn earth_weight_string into a float (number)
    earth_weight_float=float(earth_weight_str)
    #calculate mars_weight_float
    mar_weight_float=earth_weight_float*MARS_MULTIPLE
    #print out our anwer
    print("The equivalent weight on Mars: " +  str(mar_weight_float))
if __name__ == '__main__':
    main()