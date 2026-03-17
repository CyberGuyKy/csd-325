#Kyle Hughes
#3/14/26
#Assignment 1.3
#Short code using user input and loops to repeat message until complete.

def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles = bottles - 1
        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.")
        print()

    # Last bottle message
    print(f"1 bottle of beer on the wall, 1 bottle of beer.")
    print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall.")
    print()


# Main program
while True:
    try:
        bottles = int(input("Enter number of bottles: "))
        if bottles < 1:
            print("Please enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
countdown(bottles)
print("Time to buy more bottles of beer.")
