class NGram:
    
# |----------------------------------------------------------------------------|
# createBiGram
# |----------------------------------------------------------------------------|
    def createBiGram(self, strList):
        '''
        get the bigrams of all the words accept first word
        Input: list of string
        Output: list of tuples
        '''
        biGramList=[]
        for index, word in enumerate(strList):
            if not index==0:
                biGramList.append((word, strList[index-1]))
            #if index -ends
        #for index, word -ends
        return biGramList
        
# |--------------------------------createBiGram---------------------------------|    
# |----------------------------------------------------------------------------|
# noSmoothing
# |----------------------------------------------------------------------------|
    def noSmoothing(self, biGramList, uniGramDict, biGramDict):
        '''
        Probability = P(Cw-1 Cw)/P(Cw-1)
        Input:  List of bigram in the form of tuple,
                {unique_unigrams (Vocab): count_Ci} dictionary
                {unique_bigrams: Count(Cwi-1 Cwi)}
        Output: 
        '''
        probDict = {}
        for biGram in biGramList:
            nextWord, prevWord = biGram
            #print(nextWord, prevWord)
            biGramCount = biGramDict[biGram]
            prevWordCount = uniGramDict[prevWord]
            probDict[biGram]=biGramCount/prevWordCount
        #for biGram -ends
        return probDict
# |--------------------------------noSmoothing---------------------------------|
# |----------------------------------------------------------------------------|
# add1Smoothing
# |----------------------------------------------------------------------------|
    def add1Smoothing(self, biGramList, uniGramDict, biGramDict, V):

        '''
        C* = ((C(Wi-1 Wi)+1)*C(wi-1))/(C(Wi-1)+V)
        '''
        probStarDict = {}
        cStarDict = {}
        for biGram in biGramList:
            word, prevWord = biGram
            cStarDict[biGram], probStarDict[biGram]=self.addOneSmoothingWords(word, prevWord, biGramDict, uniGramDict, V)
        #for biGram -ends
        cStarDict[biGram], probStarDict[biGram]=self.addOneSmoothingWords(word, prevWord, biGramDict, uniGramDict, V)

        return probStarDict, cStarDict
# |--------------------------------add1Smoothing--------------------------------|
# |----------------------------------------------------------------------------|
# addOneSmoothingWords
# |----------------------------------------------------------------------------|
    def addOneSmoothingWords(self, word, prevWord, biGramDict, uniGramDict, V):
        '''
        
        '''
        biGram = word, prevWord
        if biGram in biGramDict:
            biGramCount = biGramDict[biGram]
        else:
            biGramCount = 0
        if prevWord in uniGramDict:
            prevWordCount = uniGramDict[prevWord]
            cStar = ((biGramCount+1)*prevWordCount)/(prevWordCount+V)
            probStar = cStar/prevWordCount
        else:
            cStar = 0
            probStar = 0
        return cStar, probStar
# |--------------------------------addOneSmoothingWords---------------------------------|
    
# |----------------------------------------------------------------------------|
# goodTuringDiscounting
# |----------------------------------------------------------------------------|
    def goodTuring(self, biGramList, uniGramDict, biGramDict, unigramCount, biGramCount):
        '''
        
        '''
        bucketDict = self.createBucket(biGramList, biGramDict, unigramCount, biGramCount)
#         # debug
#         print("bucketDict =\n {}".format(dict(sorted(bucketDict.items()))))
#         # debug -ends
        pStarDict = {}
        cStarDict = {}
        nXiFi = len(biGramList)
        for bigram in biGramList:
            count = biGramDict[bigram]
            nextCount = count+1
            if nextCount in bucketDict:
                cStarDict[bigram]=((count+1)*bucketDict[count+1])/bucketDict[count]
            else:
                cStarDict[bigram]=0
            #if -ends
            pStarDict[bigram]= cStarDict[bigram]/nXiFi  
        #for -ends
        bucket0Prob = bucketDict[1]/nXiFi
        return pStarDict, cStarDict, bucket0Prob
# |--------------------------------goodTuring---------------------------------|
# |----------------------------------------------------------------------------|
# createBucket
# |----------------------------------------------------------------------------|
    def createBucket(self, biGramList, biGramDict, unigramCount, biGramCount):
        '''
        
        '''
        bucketDict = {}
        for tup in biGramDict:
            
            count = biGramDict[tup]
            if count in bucketDict:
                bucketDict[count]+=1
            else:
                bucketDict[count]=1
            #if -ends
        #for tup -ends
        bucketDict[0]=unigramCount*unigramCount-biGramCount
        return bucketDict
# |--------------------------------createBucket---------------------------------|
    
