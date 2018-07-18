import csv
import argparse
from fuzzywuzzy import fuzz
import time

parser = argparse.ArgumentParser()
parser.add_argument('-1', '--fileName1', help='the CSV file of old headings with authorized form of the headings. optional - if not provided, the script will ask for input')
parser.add_argument('-2', '--fileName2', help='the CSV file of new headings. optional - if not provided, the script will ask for input')
parser.add_argument('-t', '--threshold', help='the threshold (e.g. \'90\' means the strings are 90% similar and 10% different ). optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.fileName1:
    fileName1 = args.fileName1
else:
    fileName1 = raw_input('Enter the file name of the CSV of old headings with authorized form of the headings (including \'.csv\'): ')
if args.fileName2:
    fileName2 = args.fileName2
else:
    fileName2 = raw_input('Enter the file name of the CSV of new headings (including \'.csv\'): ')
if args.threshold:
    threshold = int(args.threshold)
else:
    threshold = int(raw_input('Enter threshold (e.g. \'90\' means the strings are 90% similar and 10% different ): '))

startTime = time.time()

f=csv.writer(open('stringNearMatchesNewAndOld.csv','wb'))
f.writerow(['percentage']+['string1']+['stringType1']+['string2']+['stringType2']+['authorizedString'])

completeNearMatches = []
newHeadings = []
allHeadings = []
matchedHeadings = []

with open(fileName2) as csvfile2:
    reader = csv.DictReader(csvfile2)
    for row in reader:
        string = row['string']
        stringType = 'new'
        authorizedString = ''
        stringHeadingTuple = (string, stringType, authorizedString)
        allHeadings.append(stringHeadingTuple)
        newHeadings.append(stringHeadingTuple)

with open(fileName1) as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        string = row['string']
        stringType = 'old'
        if row['authorizedString'] != '':
            authorizedString = row['authorizedString']
        else:
            authorizedString = ''
        stringHeadingTuple = (string, stringType, authorizedString)
        allHeadings.append(stringHeadingTuple)


for heading in newHeadings:
    string = heading[0]
    stringType = heading[1]
    string2 = ''
    stringType2 = ''
    authorizedString = ''
    for heading2 in allHeadings:
        string2 = heading2[0]
        stringType2 = heading2[1]
        authorizedString = heading2[2]
        if string != string2:
            ratio = fuzz.ratio(string, string2)
            partialRatio = fuzz.partial_ratio(string, string2)
            tokenSort = fuzz.token_sort_ratio(string, string2)
            tokenSet = fuzz.token_set_ratio(string, string2)
            avg = (ratio+partialRatio+tokenSort+tokenSet)/4
            if avg > threshold:
                if string not in matchedHeadings:
                    f.writerow([]+[]+[]+[]+[]+[])
                    matchedHeadings.append(string)
                nearMatch = [avg, string, stringType, string2, stringType2, authorizedString]
                reversedNearMatch = [avg, string2, stringType2, string, stringType, authorizedString]
                if nearMatch not in completeNearMatches:
                    if reversedNearMatch not in completeNearMatches:
                        print nearMatch
                        completeNearMatches.append(nearMatch)
                        f.writerow([nearMatch[0]]+[nearMatch[1]]+[nearMatch[2]]+[nearMatch[3]]+[nearMatch[4]]+[nearMatch[5]])

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)
