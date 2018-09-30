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

    