# we can use single and double quotes to define a string acc to condn

course = "Python's for begineer"
revised_name = '"Python" for begineer'
print(course)
print(revised_name)


# for multiple-line string => triple quotes('''  ''')

rev_course = '''
Hi John!

This is the first email to you

Thank You!

The Support Team

'''

print(rev_course)


# Retrieving the charactes from a String

name = "Python for Begineers"

print(name[0])  # extract the 0th index val
print(name[11])

# we can also extract the char from end of str => by using -ve index
print(name[-1])
print(name[-2])

# to extract a range of character
print(name[0: 3])  # it will extract the char from 0 to 2 except 3

print(name[0:]) # extract from 0th index to last
print(name[1:])

print(name[:5]) # will consider the start index as 0


# to make the copy of our String var => [:]

another = name[:]
print(another)


# A Question

j_name = "Jeniffer"
print(j_name[1:-1])   # eniffe
