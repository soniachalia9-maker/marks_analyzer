import numpy as np

# Student marks (out of 100)
marks = np.array([78, 45, 89, 67, 90, 33, 56])

print("Student Marks:", marks)

# Average marks
average = np.mean(marks)
print("Average Marks:", average)

# Highest & Lowest
highest = np.max(marks)
lowest = np.min(marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Pass / Fail (pass >= 40)
result = marks >= 40
print("Pass/Fail Status:", result)

# Total passed students
passed_students = np.sum(marks >= 40)
print("Total Passed Students:", passed_students)