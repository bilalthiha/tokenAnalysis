import nltk
import os
import sys
import glob
from pathlib import Path
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

#module global for total number of tokens, files and filelist
totalTokens = 0
totalFiles = 0
fileList = []
maxTokenSize = 0
maxTokenByteSize = 0
minTokenSize = 10
minTokenByteSize = 100
#================== Functions=======================
def initWorkingDir(inPath):
    #change working directory
    os.chdir(inPath)    

def initFileList(inPath):
    global fileList
    global totalFiles    
    fileList = os.listdir(inPath)
    totalFiles = len(fileList)

def countFileList():
    global totalFiles
    return totalFiles
    

def countTokensInAFile(fileName):
    global maxTokenSize
    global minTokenSize
    global maxTokenByteSize
    global minTokenByteSize
    #count terms in a file
    #open the file and get its contents
    curFile = open(fileName, 'r', encoding ='utf-8')
    content = curFile.read()
    #print(content)
    curFile.close()

    #tokenize content
    tkzr = RegexpTokenizer(r'\w+')
    tokenizedWords = tkzr.tokenize(content)
    #print("Tokenized words are: " + str(tokenizedWords))

    #remove stop words
    stopWords = set(stopwords.words("english"))
    filteredWords=[]
    for w in tokenizedWords:
        if w not in stopWords:
            filteredWords.append(w)
    #print("Filtered words are: " + str(filteredWords))
    #print(len(filteredWords))

    #update min and max token sizes
    for i in filteredWords:
        if(minTokenSize > len(i)):
            minTokenSize = len(i)
            
        if(maxTokenSize < len(i)):
            maxTokenSize = len(i)

        if(minTokenByteSize > sys.getsizeof(i)):
            minTokenByteSize = sys.getsizeof(i)
            
        if(maxTokenByteSize < sys.getsizeof(i)):
            maxTokenByteSize = sys.getsizeof(i)
            
    return (len(filteredWords))

def countTokensInAllFiles():
    global totalTokens
    for i in fileList:
        totalTokens += countTokensInAFile(i)
    return totalTokens

def getMinTokenSize():
    global minTokenSize
    return minTokenSize

def getMaxTokenSize():
    global maxTokenSize
    return maxTokenSize

def getMinTokenByteSize():
    global minTokenByteSize
    return minTokenByteSize

def getMaxTokenByteSize():
    global maxTokenByteSize
    return maxTokenByteSize

def cleanPrevOutputFiles():
    flName2Del = ''
    #get list of files with 'out_' prefix
    obsFileList = glob.glob("out_*.txt")
    #print(obsFileList)
    while (len(obsFileList) > 0):
        flName2Del = obsFileList.pop(0)
        os.remove(flName2Del)

#================== End of Functions ===============

