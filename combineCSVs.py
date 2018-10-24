import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--baseFileName', help='the base file name for the files to be combined. optional - if not provided, the script will ask for input')
parser.add_argument('-s', '--suffix', help='the suffix that exists after the file number in the file name. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.baseFileName:
    baseFileName = args.baseFileName
else:
    baseFileName = raw_input('Enter the base file name for the files to be combined: ')
if args.suffix:
    suffix = args.suffix
else:
    suffix = raw_input('Enter the suffix that exists after the file number in the file name: ')

f = csv.writer(open(baseFileName + suffix + 'Combined.csv', 'wb'))

fileNum = 1
file = baseFileName +str(fileNum) + suffix + '.csv'

while Path(file).is_file() == True:
    print file
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        if fileNum > 1:
            reader.next()
        for row in reader:
            f.writerow(row)
    fileNum += 1
    file = baseFileName +str(fileNum) + suffix + '.csv'
