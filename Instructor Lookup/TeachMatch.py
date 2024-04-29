import csv

classTeachDict = {}

with open(r"C:\Users\eliza\PycharmProjects\ODL\Class2Teach.csv", 'r', encoding= "utf-8") as readfile:
    csvreader = csv.reader(readfile)
    next(csvreader)  # skips first line (labels)
    for row in csvreader:
        # checks if key already in dict, adds values to a list for duplicates
        if row[3] in classTeachDict:
            classTeachDict[row[3]].append(row[4])
        else:
            classTeachDict[row[3]] = [row[4]]

# join dict values with ;
for key in classTeachDict:
    classTeachDict[key] = "; ".join(classTeachDict[key])

# open courses we need and split them into list items
with open("peepList", 'r') as readfile:
    peopleList = readfile.read().split("\n")

# search for match in dict, print instructor name(s) if present
for code in peopleList:
    if code in classTeachDict:
        if classTeachDict[code] != "-":
            print(classTeachDict[code])
        else:
            print("")
    else:
        print("")