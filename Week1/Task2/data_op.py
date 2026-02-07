grades=[34,25,1,5,73,2,9,25,0,3,56,19,12,8,45,19,67,34,88,21]
# Adding a new grade
grades.append(95)

# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade:.2f}")

# Finding the highest and lowest grades
highest_grade = max(grades)
lowest_grade = min(grades)
print(f"Highest Grade: {highest_grade}")

grades.sort()  ## Sorts the list in ascending order
print(grades)

# Removing duplicates from the list by converting it to a set and back to a list
grades = list(set(grades))
print(grades)