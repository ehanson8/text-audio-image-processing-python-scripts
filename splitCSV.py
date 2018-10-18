import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='the CSV file to split. optional - if not provided, the script will ask for input')
parser.add_argument('-n', '--num', help='the number of rows to include in each file. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    file = args.file
else:
    file = raw_input('Enter the CSV file to split: ')
if args.num:
    num = args.num
else:
    num = raw_input('Enter the number of rows to include in each file: ')

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames

baseFileName = file.replace('.csv','')
num = int(num)

csvfile = open(file).readlines()
filenum = 1
for i in range(len(csvfile)):
    if i % num == 0:
        f = open(baseFileName + str(filenum) + '.csv', 'wb')
        if filenum != 1:
            f.write(str(header).replace('[','').replace(']','').replace('\'',''))
            f.write('\n')
        f.writelines(csvfile[i:i+num])
        filenum += 1
