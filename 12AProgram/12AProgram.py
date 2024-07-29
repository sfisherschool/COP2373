import numpy as np
import pandas as pd

# Load the data from the CSV file into a numpy array
grades_df = pd.read_csv('grades.csv')
grades = grades_df.to_numpy()

# Print the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(grades_df.head())

# Calculate and print statistics for each exam (columns)
for i in range(grades.shape[1]):
    exam_scores = grades[:, i]
    print(f"\nStatistics for Exam {i+1}:")
    print(f"Mean: {np.mean(exam_scores):.2f}")
    print(f"Median: {np.median(exam_scores):.2f}")
    print(f"Standard Deviation: {np.std(exam_scores):.2f}")
    print(f"Minimum: {np.min(exam_scores):.2f}")
    print(f"Maximum: {np.max(exam_scores):.2f}")

# Calculate and print overall statistics for the entire dataset (all exams combined)
all_scores = grades.flatten()
print("\nOverall Statistics for All Exams Combined:")
print(f"Mean: {np.mean(all_scores):.2f}")
print(f"Median: {np.median(all_scores):.2f}")
print(f"Standard Deviation: {np.std(all_scores):.2f}")
print(f"Minimum: {np.min(all_scores):.2f}")
print(f"Maximum: {np.max(all_scores):.2f}")

# Determine and print the number of students who passed and failed each exam
passing_grade = 60
for i in range(grades.shape[1]):
    exam_scores = grades[:, i]
    passed = np.sum(exam_scores >= passing_grade)
    failed = np.sum(exam_scores < passing_grade)
    print(f"\nExam {i+1}:")
    print(f"Number of students who passed: {passed}")
    print(f"Number of students who failed: {failed}")

# Calculate and print the overall pass percentage across all exams
total_students = grades.shape[0] * grades.shape[1]
total_passed = np.sum(all_scores >= passing_grade)
pass_percentage = (total_passed / total_students) * 100
print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")
