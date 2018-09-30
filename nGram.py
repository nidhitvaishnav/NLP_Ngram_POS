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

