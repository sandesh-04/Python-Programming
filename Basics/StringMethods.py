course = "Python for Beginner"

# len => to calculate the length of String
# These len,print are the general purpose functions they do not specifically belongs
# to any of the Strings or number or any kind of objects
print(len(course))

# Methods => are accessed by using the . operator
# These are the functions that are Specific to Strings that's why they are called
# as methods

# upper() & lower()
print(course.upper())
print(course.lower())
print(course)  # do not modify the actual String


# find() => to find the sequence of the char from String
print(course.find('P')) # give 1st occurrence
print(course.find('p')) # -1 as this char is not present & Python is case-sensitive
print(course.find('Beginner')) # 11


# replace() => to replace something from String to something else
print(course.replace('Beginner', 'Absolute Beginner'))
print(course.replace('B', 'H'))


# in => to check if the character is present in String or not
print('Python' in course)  # True
