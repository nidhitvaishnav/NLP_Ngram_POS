class POS_Tagging:
 
# |----------------------------------------------------------------------------|
# createWordTagDict
# |----------------------------------------------------------------------------|
    def createTagTagList(self, wordTagList):

        '''
        get the word,tag of all the words accept first word
        Input: list of (word,Tag) tuple
        Output: list of (tag_current, tag_prev) tuple
        '''
        tagTagList = []
        for index, item in enumerate(wordTagList):
            if not index==0:
                word, tag = item
                prevWord, prevTag =wordTagList[index-1] 
                tagTagList.append((tag, prevTag))
        #for index, word -ends
        return  tagTagList
        
# |--------------------------createWordTagDict---------------------------------|
# |----------------------------------------------------------------------------|
# naiveBayesClassification
# |----------------------------------------------------------------------------|
    def naiveBayesClassification(self, wordTagList, tagDict, wordTagDict, tagTagDict):
        '''
        
        '''
        probWTDict = {}
        lenWTList = len(wordTagList)
        V = len(tagDict)
        probTagTagDict = self.getTagTagDictProbability(tagDict, tagTagDict)
        for index, wordTag in enumerate(wordTagList):
            curWord, curTag = wordTag
            probWgivenT = wordTagDict[wordTag]/tagDict[curTag]
            probWTDict[wordTag] = probWgivenT
            #if -ends
        #for -ends
        return probWTDict, probTagTagDict
                
        
# |--------------------------------naiveBayesClassification---------------------------------|
# |----------------------------------------------------------------------------|
# getTagTagDictProbability
# |----------------------------------------------------------------------------|
    def getTagTagDictProbability(self,tagDict, tagTagDict):
        '''
        
        '''
        V = len(tagDict)
        probTagTagDict = {}
        for prevTag in tagDict:
            for curTag in tagDict:
                if (curTag, prevTag) in tagTagDict:
                    probTgivenPrevT = (tagTagDict[(curTag, prevTag)]+1)/(tagDict[prevTag]+V)
                else:
                    probTgivenPrevT=1/(tagDict[prevTag]+V)
                    
                #if -ends
                probTagTagDict[(curTag, prevTag)]=probTgivenPrevT
            #for -ends
        #for -ends
        return probTagTagDict    
# |--------------------------------getTagTagDictProbability---------------------------------|
    
# |----------------------------------------------------------------------------|
# findOtherAllWordTags
# |----------------------------------------------------------------------------|
    def findOtherAllWordTags(self, inWord, wordTagDict):
        '''
        
        '''
        currentWordTagList = []
        for key in wordTagDict:
            word, tag = key
            if word==inWord:
                currentWordTagList.append(tag)
            #if -ends
        #for -ends
        return currentWordTagList
        
# |--------------------------findOtherAllWordTags------------------------------|
    