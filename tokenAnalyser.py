import helper
import os
from pathlib import Path

#get input (inputPath, inputBlockSize)
#path to files
print('Please key in directory to the input text files')
inputPath = input()
print('Echo input: ' + inputPath)

#handle invalid path
givenPath = Path(inputPath)
if((givenPath.exists()) == False):
    print('Invalid given directory of input dataset. Nothing to do. Program ends.')
    sys.exit()

#init working directory
helper.initWorkingDir(inputPath)

#clean previous output files
helper.cleanPrevOutputFiles()

#provide directory for helper to process files
fileList = helper.initFileList(inputPath)

#get total number of files
totalF = helper.countFileList()

#get total number of terms in files
totalT = helper.countTokensInAllFiles()

#get min and max token sizes
minT = helper.getMinTokenSize()
maxT = helper.getMaxTokenSize()

#get min and max token sizes
minTB = helper.getMinTokenByteSize()
maxTB = helper.getMaxTokenByteSize()

#calculate average terms per doc
avg = totalT/totalF

#output analysis data
outFile = open('out_tokenAnalysis.txt', 'a', encoding ='utf-8')
outFile.write('Total number of documents is ' + str(totalF) + '\n')
outFile.write('Total Number of terms is ' + str(totalT) + '\n')
outFile.write('Average terms per document is ' + str(avg) + '\n')
outFile.write('Min token size (characters) is ' + str(minT) + '\n')
outFile.write('Min token byte size (bytes) is ' + str(minTB) + '\n')
outFile.write('Max token size (characters) is ' + str(maxT)+ '\n')
outFile.write('Max token byte size (bytes) is ' + str(maxTB)+ '\n')
outFile.close()

print('tokens are analysed from ' + inputPath + ' and the analysis is output as out_tokenAnalysis.txt in the same folder')

    
    


