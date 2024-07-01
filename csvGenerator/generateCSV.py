import csv


def write_grades_to_csv(num_students):
    # Open the grades.csv file in write mode
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop over the number of students
        for i in range(num_students):
            # Get the student data
            first_name = input("Enter the first name of student {}: ".format(i + 1))
            last_name = input("Enter the last name of student {}: ".format(i + 1))

            while True:
                try:
                    exam1 = int(input("Enter the grade for Exam 1 of student {}: ".format(i + 1)))
                    break
                # If we did not get an integer correct the user
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    exam2 = int(input("Enter the grade for Exam 2 of student {}: ".format(i + 1)))
                    break
                # If we did not get an integer correct the user
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    exam3 = int(input("Enter the grade for Exam 3 of student {}: ".format(i + 1)))
                    break
                # If we did not get an integer correct the user
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Write the student data
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Student and test data has been written to grades.csv")


def main():
    # Get the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            break
        # If we did not get an integer correct the user
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Call the function to write grades to CSV
    write_grades_to_csv(num_students)


# Call the main function
main()
