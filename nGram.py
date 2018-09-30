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
    
