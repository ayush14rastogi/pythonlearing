# function with 2 keyword arguments grade and school
# In a function, arguments can have default values.

def student(name, age, grade="Five", school="ABC School"):
    print('Student Details:', name, age, grade, school)

# without passing grade and school
# Passing only the mandatory arguments
student('Jon', 12)

# Output: Student Details: Jon 12 Five ABC School