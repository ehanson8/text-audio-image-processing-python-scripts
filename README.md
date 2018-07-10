# text-audio-image-processing
Scripts for processing audio and images

#### [dhashImageComparison.py](dhashImageComparison.py)
Based on user input, this script creates dhashes for all of the image files in the specified directory and then compares them using a BK-tree and creates a CSV file of all dhashes matches that are below the specified threshold (e.g. '40' means the dhashes are 40% different and 60% similar).

#### [ocrDirectoryOfImages.py](ocrDirectoryOfImages.py)
Based on user input, this script generates an optical character recognition text file for all of the jpgs in a specified directory.

#### [transcribeAudioFile.py](transcribeAudioFile.py)
This script generates a rough, unformatted transcript of a specified MP3 using the free Wit ([https://wit.ai/](https://wit.ai/)) speech-to-text API. The script requires a secrets.py file in the same directory that must contain the following text:
```
        filePath ='[The file path where the source MP3]'
        witKey ='[The 'Server Access Token' on the 'Settings' page from your Wit.ai account]'

```
