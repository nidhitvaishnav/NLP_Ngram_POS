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

