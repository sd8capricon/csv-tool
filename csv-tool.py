import argparse
import csv
import io


f = open("hw_25000.csv", "r")

# count the number of rows in the file


def count(file: io.TextIOWrapper):
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        count += 1
    f.seek(0)
    return count


# mean of a given column
def mean(file: io.TextIOWrapper, column: str):
    reader = csv.DictReader(file)
    sum = 0
    count = 0
    for row in reader:
        try:  # try to convert to float
            if (row[column] == ""):
                continue
            sum += float(row[column])
            count += 1
        except ValueError as e:  # if fails, print error
            print(e.args)
            print("all value should be numeric")
            return None
    f.seek(0)
    return sum / count


# filter the file by a given column and value


def filter(file: io.TextIOWrapper, column: str, value: float):
    reader = csv.DictReader(file)
    temp = []
    for row in reader:
        if (float(row[column]) >= value):
            temp.append(row)
    return temp


# print count
# print(count(f))

# print filter
# arr = filter(f, "Height(Inches)", 71.5)
# for i in arr:
#     print(i)

print(mean(f, "Height(Inches)"))
