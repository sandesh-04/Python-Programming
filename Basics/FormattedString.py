# formatted Strings are used to dynamically generate some text from out variables

first = "John"
last = "Smith"

message = first + ' [' + last + '] is a coder'
print(message)
# this is not the ideal way of doing this here is where we use formatted Str

msg = f'{first} [{last}] is a coder'
# {} = are placeholder that holds our variables
print(msg)
