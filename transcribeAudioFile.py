import json
import time
import requests
from pydub import AudioSegment
import os
import secrets

startTime = time.time()

witKey = secrets.witKey
filePath = secrets.filePath

file = raw_input('Enter file name (including \'.mp3\')')
file = 'MS150_CarrieJohnsonInterview_Tape1_SideA.mp3'
fullFilePath = filePath+file

sound = AudioSegment.from_mp3(fullFilePath)
f = open(file+'.txt', 'wb')
for i in range(1, 31):
    sleepTime = 5
    print 'waiting '+str(sleepTime)+' seconds'
    time.sleep(sleepTime)
    segmentStartTime = time.time()
    split = len(sound) / 30
    splitStartPoint = split * (i - 1)
    splitEndPoint = split * i
    if splitEndPoint > len(sound):
        splitEndPoint = len(sound)
    s, ms = divmod(splitEndPoint, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    timeStamp = '%d:%02d:%02d.%02d' % (h, m, s, ms)

    fileSegment = sound[splitStartPoint:splitEndPoint]
    fileName = file.replace('.','_'+str(i)+'.')
    fileSegment.export(filePath+fileName, format="mp3")
    fullFilePath = filePath+fileName

    soundFile = open(fullFilePath, 'rb')
    url = "https://api.wit.ai/speech?v=20160526"
    headers = {'Authorization': 'Bearer '+witKey, 'Content-Type': 'audio/mpeg3'}
    print fileName
    results = requests.post(url, data=soundFile, headers=headers).json()
    while '_text' not in results:
        print json.dumps(results)
        sleepTime = 5
        print 'waiting '+str(sleepTime)+' seconds'
        time.sleep(sleepTime)
        soundFile = open(fullFilePath, 'rb')
        results = requests.post(url, data=soundFile, headers=headers).json()
    results = results['_text']
    f = open(file+'.txt', 'a')
    f.write('\n'+timeStamp+'\n'+results)
    print 'Segment transcript created'
    os.remove(fullFilePath)

    elapsedTime = time.time() - segmentStartTime
    m, s = divmod(elapsedTime, 60)
    h, m = divmod(m, 60)
    print 'Segment processing time: ', '%d:%02d:%02d' % (h, m, s)

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)
