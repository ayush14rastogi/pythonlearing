def student(name, grade="Five", age):
    print('Student Details:', name, grade, age)

student('Jon', 'Six', 12)
# Output: SyntaxError: non-default argument follows default argument

def pick(l: list, index: int) -> int:
    return l[index]