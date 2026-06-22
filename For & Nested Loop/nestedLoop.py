for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')



numbers = [5, 2, 5, 2, 2]

# for z in numbers:
#     print('*' * z)

for a_count in numbers:
    output = ''
    for count in range(a_count):
        output += 'x'
    print(output)