import pandas as pd

def read_grades_from_csv():
    # Read the grades.csv file
    with open('grades.csv', 'r') as file:
        df = pd.read_csv(file)

    # Display the data in tabular format
    print(df)

# Call the function to read grades from CSV
read_grades_from_csv()
