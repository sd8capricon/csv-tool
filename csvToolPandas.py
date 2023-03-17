import argparse
import pandas as pd
import io

parser = argparse.ArgumentParser(
    description="CSV Tool")
parser.add_argument("file", help="path to CSV file")
parser.add_argument("-c", "--command", help="Command to run: \n count - count the number of rows in the file \n mean - mean of a given column \n filter - filter the file by a given column and value\n sort - sort the file by a given column\n std - standard deviation of a given column\n exit - exit the program")
parser.add_argument("-f", "--filter", help="Filter to use")
parser.add_argument("-col", "--column", help="Column to use")

loopParse = argparse.ArgumentParser(description="CSV Tool")
loopParse.add_argument("command", help="Command to run")
loopParse.add_argument("-f", "--filter", help="Filter to use")
loopParse.add_argument("-col", "--column", help="Column to use")

# count the number of rows in the file


def count(df: pd.DataFrame):
    return df.shape[0]


# check if a column exists in the file
def checkColumn(df: pd.DataFrame, column: str):
    if column in df.columns:
        return True
    return False


# mean of a given column


def mean(df: pd.DataFrame, column: str):
    if (checkColumn(df, column) == False):
        print("Column does not exist")
        return None
    return df[column].mean()


# filter the file by a given column and value


def filter(df: pd.DataFrame, column: str, value: float):
    if (checkColumn(df, column) == False):
        print("Column does not exist")
        return None
    if (value == None):
        return None
    return df[df[column] == value]


# sort the file by a given column


def sort(df: pd.DataFrame, column: str):
    if (checkColumn(df, column) == False):
        print("Column does not exist")
        return None
    return df.sort_values(by=[column])

# Standard Deviation of a given column


def standardDeviation(df: pd.DataFrame, column: str):
    if (checkColumn(df, column) == False):
        print("Column does not exist")
        return None
    return df[column].std()


if __name__ == "__main__":
    args = parser.parse_args()
    try:
        df = pd.read_csv(args.file)
        print("Welcome to the CSV Tool\npositional arguments:\n\tcommand - Command to run(count, mean, filter, std, sort, exit)\noptional arguments:\n\t-h, --help - show this help message and exit\n\t-f FILTER, --filter FILTER - Filter to use\n\t-col COLUMN, --column COLUMN - Column to use")
        while True:
            if args.command == "count":
                print(count(df))
            elif args.command == "mean":
                print(mean(df, args.column))
            elif args.command == "filter":
                print(filter(df, args.column, args.filter))
            elif args.command == "sort":
                print(sort(df, args.column))
            elif args.command == "std":
                print(standardDeviation(df, args.column))
            elif args.command == "exit":
                print("Exiting...")
                break
            try:
                args = loopParse.parse_args(input("csv-tool> ").split())
            except SystemExit:
                pass
    except FileNotFoundError as e:
        print("File not found")
