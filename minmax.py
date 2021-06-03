import csv
from collections import Counter

csvFile = input("Which csv file do you want to open?")

with open(csvFile, newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = []

for line in range(len(fileData)):
    num = fileData[line][1]
    newData.append(float(num))

newData.sort()

n = len(newData)

mini = newData[0]

maxi = newData[int(n-1)]

ranges = maxi - mini

total = 0

print(n)

for x in newData:
    total = total + x

mean = total / n

if(n % 2 == 0):
    up = newData[int(n/2)]
    down = newData[int(n/2)+1]
    m = len(newData) / 2
    k = m + 1
    z = up + down
    med = z / 2
    print("Median: "+str(med))
    secondUp = newData[int(m/2)]
    secondDown = newData[int(m/2)+1]
    thirdUp = newData[int(m*1.5)]
    thirdDown = newData[int(m*1.5)+1]
    y = secondUp + secondDown
    x = thirdUp + thirdDown
    firstQuartile = y / 2
    thirdQuartile = x / 2
    print("First Quartile: "+str(firstQuartile))
    print("Third Quartile: "+str(thirdQuartile))
else:
    actual = float(n/2)+0.5
    m = len(newData) / 2
    secondActual = float(m/2)+0.75
    thirdActual = float(m*1.5)+0.25
    median = newData[int(actual)-1]
    firstQuartile = newData[int(secondActual)-1]
    thirdQuartile = newData[int(thirdActual)-1]
    print("Median: "+str(median))
    print("First Quartile: "+str(firstQuartile))
    print("Third Quartile: "+str(thirdQuartile))

print("Mean: "+ str(mean))

print("Minimum: "+str(mini))

print("Maximum: "+str(maxi))

print("Range: "+str(ranges))

# data = Counter(newData)

# modeDataForRange = {
#     "0-60": 0,
#     "60-70": 0,
#     "70-80": 0
# }

# for height, occurrence in data.items():
#     if 50 < float(height) < 60:
#         modeDataForRange["50-60"] += occurrence
#     elif 60 < float(height) < 70:
#         modeDataForRange["60-70"] += occurrence
#     elif 70 < float(height) < 80:
#         modeDataForRange["70-80"] += occurrence
    
# modeRange, modeOccurrence = 0, 0

# for range, occurrence in modeDataForRange.items():
#     if occurrence > modeOccurrence:
#         modeRange, modeOccurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence

# mode = float((modeRange[0]+modeRange[1])/2)

# print(f"Mode: {mode: 2f}")