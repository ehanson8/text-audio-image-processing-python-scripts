# text-audio-image-processing
Scripts for processing audio and images

#### [dhashImageComparison.py](dhashImageComparison.py)
Based on user input, creates dhashes for all of the image files in the specified directory and then compares them using a BK-tree and creates a CSV file of all dhashes matches that are below the specified threshold (e.g. '40' means the dhashes are 40% different and 60% similar).

#### [ocrDirectoryOfImages.py](ocrDirectoryOfImages.py)
Based on user input, generates an optical character recognition text file for all of the jpgs in a specified directory.

#### [stringComparisonFromCSV.py](stringComparisonFromCSV.py)
Based on a specified file and a specified threshold (e.g. '90' means the strings are 90% similar and 10% different), compares each string against every other string in the file, identifies all strings with a similarity above the specified threshold, and prints it to a new CSV file.

#### [stringComparisonFromCSVOldAndNew.py](stringComparisonFromCSVOldAndNew.py)
Based on a specified files of new and old strings and a specified threshold (e.g. '90' means the strings are 90% similar and 10% different), compares each string against every other string in the new strings file, identifies all strings with a similarity above the specified threshold, and prints it to a new CSV file. It also compares each string to a CSV file of old strings that have previously received an authorized form (e.g. adding new name headings to an existing authority file)

#### [transcribeAudioFile.py](transcribeAudioFile.py)
Generates a rough, unformatted transcript of a specified MP3 using the free Wit ([https://wit.ai/](https://wit.ai/)) speech-to-text API. The script requires a secrets.py file in the same directory that must contain the following text:
```
        filePath ='[The file path where the source MP3]'
        witKey ='[The 'Server Access Token' on the 'Settings' page from your Wit.ai account]'

```
