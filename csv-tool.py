import argparse
import csv
import io

parser = argparse.ArgumentParser(
    description="CSV Tool")
parser.add_argument("file", help="path to CSV file")
parser.add_argument("-c", "--command", help="Command to run: \n count - count the number of rows in the file \n mean - mean of a given column \n filter - filter the file by a given column and value")
parser.add_argument("-f", "--filter", help="Filter to use")
parser.add_argument("-col", "--column", help="Column to use")

loopParse = argparse.ArgumentParser(description="CSV Tool")
loopParse.add_argument("command", help="Command to run")
loopParse.add_argument("-f", "--filter", help="Filter to use")
loopParse.add_argument("-col", "--column", help="Column to use")

# count the number of rows in the file


def count(file: io.TextIOWrapper):
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        count += 1
    file.seek(0)
    return count-1


# check if a column exists in the file
def checkColumn(file: io.TextIOWrapper, column: str):
    reader = csv.DictReader(file)
    row = next(reader)
    if (column in row):
        file.seek(0)
        return True
    file.seek(0)
    return False


# mean of a given column


def mean(file: io.TextIOWrapper, column: str):
    reader = csv.DictReader(file)
    sum = 0
    count = 0
    if (checkColumn(file, column) == False):
        print("Column does not exist")
        return None
    for row in reader:
        try:  # try to convert to float
            if (row[column] == ""):
                continue
            sum += float(row[column])
            count += 1
        except ValueError as e:  # if fails, print error
            print("All values should be numeric")
            return None
    file.seek(0)
    return sum / count


# filter the file by a given column and value


def filter(file: io.TextIOWrapper, column: str, value: float):
    reader = csv.DictReader(file)
    temp = []
    if (checkColumn(file, column) == False):
        print("Column does not exist")
        return None
    for row in reader:
        if (row[column] == value):
            temp.append(row)
    file.seek(0)
    return temp


if __name__ == "__main__":
    args = parser.parse_args()
    try:
        file = open(args.file, "r")
        print("Welcome to the CSV Tool\npositional arguments:\n\tcommand - Command to run\noptional arguments:\n\t-h, --help - show this help message and exit\n\t-f FILTER, --filter FILTER - Filter to use\n\t-col COLUMN, --column COLUMN - Column to use")
        while True:
            if args.command == "count":
                print(count(file))
            elif args.command == "mean":
                print(mean(file, args.column))
            elif args.command == "filter":
                print(filter(file, args.column, args.filter))
            elif args.command == "exit":
                print("Exiting...")
                break
            try:
                args = loopParse.parse_args(input("csv-tool> ").split())
            except SystemExit:
                pass
    except FileNotFoundError as e:
        print("File not found")
