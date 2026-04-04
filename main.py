import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    X=random.randint(1,99)
    Y=random.randint(1,99)
    print(f"What is {X} + {Y}?")
    answer=input("Your answer: ")
    
    if answer==str(X+Y):
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {X+Y}")
    
if __name__ == '__main__':
    main()