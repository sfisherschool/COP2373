import math


def calculate_hypotenuse():
    while True:
        try:
            # Take user input for the nearest angle in degrees
            angle_degrees = float(input("Enter the nearest angle in degrees: "))

            # Take user input for the length of the adjacent side
            adjacent_side_length = float(input("Enter the length of the adjacent side: "))

            # Check if the inputs are valid
            if angle_degrees <= 0 or angle_degrees >= 90:
                print("Error: The angle must be between 0 and 90 degrees. Please try again.")
                continue
            if adjacent_side_length <= 0:
                print("Error: The length of the adjacent side must be greater than 0. Please try again.")
                continue

            # Convert the angle from degrees to radians
            angle_radians = math.radians(angle_degrees)

            # Calculate the length of the hypotenuse
            hypotenuse_length = adjacent_side_length / math.cos(angle_radians)

            # Print the result
            print(f"The length of the hypotenuse is {hypotenuse_length} units.")

            # Exit the loop
            break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")


# Call the function
calculate_hypotenuse()
