# text-audio-image-processing

Note: Upgraded to Python 3 in 02/2019

Scripts for processing audio and images

#### [combineCSVs.py](combineCSVs.py)
Based on user input, combines several CSV file that have the same specified base file name followed by sequential numbers (e.g 'report1.csv', 'report2.csv', 'report3.csv'). A file name suffix may added if one exists after the file number (e.g. 'report1edited.csv', 'report2edited.csv', 'report3edited.csv'). Used to combine files split by [splitCSV.py](splitCSV.py).

#### [dhashImageComparison.py](dhashImageComparison.py)
Based on user input, creates dhashes for all of the image files in the specified directory and then compares them using a BK-tree and creates a CSV file of all dhashes matches that are below the specified threshold (e.g. '40' means the dhashes are 40% different and 60% similar).

#### [ocrDirectoryOfImages.py](ocrDirectoryOfImages.py)
Based on user input, generates an optical character recognition text file for all of the jpgs in a specified directory.

#### [stringComparisonFromCSV.py](stringComparisonFromCSV.py)
Based on a specified file and a specified threshold (e.g. '90' means the strings are 90% similar and 10% different), compares each string against every other string in the file, identifies all strings with a similarity above the specified threshold, and prints it to a new CSV file.

#### [stringComparisonFromCSVOldAndNew.py](stringComparisonFromCSVOldAndNew.py)
Based on a specified files of new and old strings and a specified threshold (e.g. '90' means the strings are 90% similar and 10% different), compares each string against every other string in the new strings file, identifies all strings with a similarity above the specified threshold, and prints it to a new CSV file. It also compares each string to a CSV file of old strings that have previously received an authorized form (e.g. adding new name headings to an existing authority file)

#### [splitCSV.py](splitCSV.py)
Based on user input, splits the specified CSV file into separate CSV files with specified number of rows. The header row is repeated in each new file. The files can be combined later with [combineCSVs.py](combineCSVs.py).

#### [transcribeAudioFile.py](transcribeAudioFile.py)
Generates a rough, unformatted transcript of a specified MP3 using the free Wit ([https://wit.ai/](https://wit.ai/)) speech-to-text API. The script requires a secrets.py file in the same directory that must contain the following text:
```
        filePath ='[The file path where the source MP3]'
        witKey ='[The 'Server Access Token' on the 'Settings' page from your Wit.ai account]'

```
