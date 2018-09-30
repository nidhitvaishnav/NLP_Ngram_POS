class MyUtil:
    
# |----------------------------------------------------------------------------|
# readFile
# |----------------------------------------------------------------------------|
    def readFile(self, inFile):
        '''
        
        '''
        file = open(inFile, "r")
        data=file.read().split()
        file.close()
        return data
# |--------------------------------readFile---------------------------------|
# |----------------------------------------------------------------------------|
# countWords
# |----------------------------------------------------------------------------|
    def countWords(self, strList):
        '''
        from the given list, get the unique words in the dictionary and count 
        them
        '''
        myDict = {}
        totalCountN=0
        for word in (strList):
            if word in myDict:
                myDict[word]+=1
            else:
                myDict[word]=1
            #if word -ends
            totalCountN+=1
        #for word -ends
        countV = len(myDict)
        return myDict, countV, totalCountN
        
# |--------------------------------countWords---------------------------------|
# |----------------------------------------------------------------------------|
# writeDictInFile
# |----------------------------------------------------------------------------|
    def writeProbability(self, probDict, outFIle):
        '''
        
        '''
        file = open(outFIle, "w")
        for tup in probDict:
            prevWord, nextWord = tup
            prob = probDict[tup]
            opStr = "P("+prevWord+"|"+nextWord+") = "+str(prob)+"\n"
            file.write(opStr)
        #for -ends
        file.close()
        return True
# |--------------------------------writeDictInFile-----------------------------|
# |----------------------------------------------------------------------------|
# writeAdd1SmoothingInFile
# |----------------------------------------------------------------------------|
    def writeCStarProbability(self, probDict, cStarDict, outFile):
        '''
        
        '''
        file = open(outFile, "w")
        for tup in probDict:
            prevWord, nextWord = tup
            prob = probDict[tup]
            cStar = cStarDict[tup]
            opStr = "("+prevWord+"|"+nextWord+")\t:-\tC= "+str(cStar)+"\tP= "+str(prob)+"\n"
            file.write(opStr)
        #for -ends
        file.close()
        return True
        
# |--------------------------------writeAdd1SmoothingInFile---------------------------------|
# |----------------------------------------------------------------------------|
# readPOSFile
# |----------------------------------------------------------------------------|
    def readPOSFile(self, inFile):
        '''
        
        '''
        tagList = []
        wordTagList = []
        lineList = []
        with open(inFile) as file:
            for line in file:
                tempList = line.split()
                lineList.append(tempList)
                for item in tempList:
                    word, tag = item.split("_")
                    wordTagList.append((word,tag))
                    tagList.append(tag)
            #for -ends
        #with -ends
        file.close()
        return tagList, wordTagList, lineList
# |--------------------------------readPOSFile---------------------------------|
    