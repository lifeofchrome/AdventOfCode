with open('day1input.txt', 'r') as day1inputFile:
    day1input = day1inputFile.read()

floor = 0
firstBasementPos = 0
currentPosition = 0
enteredBasement = False

for char in day1input:
    currentPosition += 1
    if char is '(':
        floor += 1
    elif char is ')':
        floor -= 1
    if floor < 0 and not enteredBasement:
        firstBasementPos = currentPosition
        enteredBasement = True


print("Part 1: " + str(floor))
print("Part 2: " + str(firstBasementPos))
