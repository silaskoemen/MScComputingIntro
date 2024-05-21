# Read in a csv file, compute the mean of each line of the csv file and print the mean to stdout 

#!/usr/bin/env python3
# USAGE: python3 compute_means.py </PATH/TO/DATA.csv> 

import csv
import sys

def read_csv_and_compute_means(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                try:
                    numbers = [float(value) for value in row]
                    if numbers:
                        mean_value = sum(numbers) / len(numbers)
                        print(f'Mean of {row} is {mean_value}')
                    else:
                        print(f'Empty row encountered: {row}')
                except ValueError:
                    print(f'Non-numeric value encountered in row: {row}')
    except FileNotFoundError:
        print(f'File not found: {file_path}')

if __name__ == "__main__":
    file_path = sys.argv[1]
    read_csv_and_compute_means(file_path)

