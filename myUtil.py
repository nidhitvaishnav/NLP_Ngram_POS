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
            if tup in cStarDict:
                cStar = cStarDict[tup]
            else:
                cStar = 0
            #if -ends
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
        wordList = []
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
                    wordList.append(word)
                    tagList.append(tag)
            #for -ends
        #with -ends
        file.close()
        return wordList, tagList, wordTagList, lineList
# |--------------------------------readPOSFile---------------------------------|
# |----------------------------------------------------------------------------|
# writeBrillsRuleFile
# |----------------------------------------------------------------------------|
    def writeBrillsRuleFile(self, brillsRules, outFile):
        '''
        
        '''
        int1 = open(outFile, 'w')
        int1.write('PREV TAG' + '\t' + 'FROM' + '\t' + 'TO' + '\t\t' + 'SCORE' + '\n\n')
     
        for i in range(len(brillsRules)):
            int1.write(str(brillsRules[i][0][0]) + "\t\t\t" + str(brillsRules[i][0][1]) + "\t\t" +
                       str(brillsRules[i][0][2]) + "\t\t" + str(brillsRules[i][1]) + "\n")
     
        int1.close()
# |--------------------------------writeBrillsRuleFile---------------------------------|
    