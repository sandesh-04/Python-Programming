# for loop is used to iterate over collection like String as it looks
#like collection of character

# using for loop we can iterate over each character of String


# here item => loop variable, in each iteration this var holds one item
for item in "Python":
    print(item)


# in python we can define list using [] brackets:
for itm in ['Mosh', 'John', 'Sarah']:
    print(itm)

for num in [1, 2, 3, 4, 5]:
    print(num)


# in pyhton we have a inbuilt function called range=>to have a range of numbers

for thing in range(10):  # whenever range fun called it created a object and
                           # we iterate over range of object
    print(thing)


for thng in range(5, 10):
    print(thng)

for thg in range(5, 10, 2):  # iterate over the gap of 2
    print(thg)


prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(total)
