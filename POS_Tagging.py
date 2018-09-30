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
        probTagTagDict = {}
        lenWTList = len(wordTagList)
        for index, wordTag in enumerate(wordTagList):
            curWord, curTag = wordTag
            if (index!=0 and (index+1)!=lenWTList):
                prevWord, prevTag = wordTagList[index-1]
                probWgivenT = (wordTagDict[wordTag])/tagDict[curTag]
                if (curTag,prevTag) in tagTagDict:
                    probTgivenPrevT = tagTagDict[(curTag, prevTag)]/tagDict[prevTag]
                else:
                    probTgivenPrevT=0
                #if -ends
                probWTDict[wordTag] = probWgivenT
                probTagTagDict[(curTag, prevTag)] = probTgivenPrevT
            #if -ends
        #for -ends
        return probWTDict, probTagTagDict
                
        
# |--------------------------------naiveBayesClassification---------------------------------|
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
    