import tesserocr
import os
import time

startTime = time.time()
filePath = raw_input('Enter file path (e.g. \'C:/sampleImages/\'): ')
files = os.listdir(filePath)
for file in files:
    print file
    if file.endswith('jpg'):
        print file
        fileName = file[:file.rindex('.')]
        imageFile = os.path.join(filePath, file)
        print imageFile
        text = tesserocr.file_to_text(imageFile)
        f=(open(filePath+fileName+'.txt', 'wb'))
        f.write(text.encode('utf-8'))
        print 'text file created'
    else:
        print 'skipped'

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ','%d:%02d:%02d' % (h, m, s)
