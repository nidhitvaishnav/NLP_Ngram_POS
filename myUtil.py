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
            opStr = "("+prevWord+"|"+nextWord+")\t:-\tC*= "+str(cStar)+"\tP*= "+str(prob)+"\n"
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
        corpusList = []
        tagList = []
        with open(inFile) as file:
            for line in file:
                tempList = line.split()
                for item in tempList:
                    word, tag = item.split("_")
                    corpusList.append(word)
                    tagList.append(tag)
            #for -ends
        #with -ends
        file.close()
        return corpusList, tagList
# |--------------------------------readPOSFile---------------------------------|
    