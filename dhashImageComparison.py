import dhash
import pybktree
import os
from PIL import Image
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filePath', help='the file path of the image. \
optional - if not provided, the script will ask for input')
parser.add_argument('-t', '--threshold', help='the threshold (e.g. \'40\' \
means the dhashes are 40% different and 60% similar). optional - if not \
provided, the script will ask for input')
args = parser.parse_args()

if args.filePath:
    filePath = args.filePath
else:
    filePath = input('Enter file path (e.g. \'C:/sampleImages/\'): ')
if args.threshold:
    threshold = int(args.threshold)
else:
    threshold = int(input('Enter threshold (e.g. \'40\' means the dhashes are \
    40% different and 60% similar): '))

hashDict = {}
hashList = []
files = os.listdir(filePath)
for file in files:
    image = Image.open(filePath + '/' + file)
    imageDhash = dhash.dhash_int(image)
    hashDict[imageDhash] = file
    hashList.append(imageDhash)

f = csv.writer(open('dhashNearMatches.csv', 'w'))
f.writerow(['percentage'] + ['dhash1'] + ['dhash2'])
completeNearMatches = []
tree = pybktree.BKTree(pybktree.hamming_distance, hashList)
for hash in hashList:
    nearMatches = tree.find(hash, threshold)
    for nearMatch in nearMatches:
        if hashDict[hash] != hashDict[nearMatch[1]]:
            print(nearMatch[0], hashDict[hash], hashDict[nearMatch[1]])
            hashTuple = (nearMatch[0], hashDict[hash], hashDict[nearMatch[1]])
            hashTupleReversed = (nearMatch[0], hashDict[nearMatch[1]],
                                 hashDict[hash])
            if hashTupleReversed not in completeNearMatches:
                completeNearMatches.append(hashTuple)
for hashTuple in completeNearMatches:
    f.writerow([hashTuple[0]] + [hashTuple[1]] + [hashTuple[2]])
