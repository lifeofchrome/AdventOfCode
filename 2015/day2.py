import re

with open('day2input.txt', 'r') as day2inputFile:
    day2input = day2inputFile.readlines()
day2input = [x.strip() for x in day2input]

totalArea = 0
totalRibbon = 0

for gift in day2input:
    dims = re.split('x', gift)
    dims = [int(x) for x in dims]

    surfaceArea = 2*dims[0]*dims[1] + 2*dims[1]*dims[2] + 2*dims[2]*dims[0]
    smallestSideArea = min(dims[0]*dims[1], dims[1]*dims[2], dims[2]*dims[0])
    totalArea += surfaceArea + smallestSideArea

    smallestSidePerimeter = min(2*dims[0] + 2*dims[1], 2*dims[1] + 2*dims[2], 2*dims[2] + 2*dims[0])
    giftVolume = dims[0]*dims[1]*dims[2]
    totalRibbon += smallestSidePerimeter + giftVolume

print("Part 1: " + str(totalArea))
print("Part 2: " + str(totalRibbon))
