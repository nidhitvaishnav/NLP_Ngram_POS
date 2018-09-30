import sys
from myUtil import MyUtil
from nGram import NGram
from POS_Tagging import POS_Tagging
class POSTaggingUI:

# |----------------------------------------------------------------------------|
# myUI
# |----------------------------------------------------------------------------|
    def myUI(self, inFile):
        '''
        
        '''
        myUtil = MyUtil()
        tagList, wordTagList, lineList = myUtil.readPOSFile(inFile)
        
        pos_Tagging = POS_Tagging()
        tagTagList = pos_Tagging.createTagTagList(wordTagList)
        # debug
        print("len(wordTagList = {}, tagTagList = {}".format(len(wordTagList), len(tagTagList)))
        # debug -ends

        #get unigram and bigram counts
        tagDict, tagCountV, tagCountN = myUtil.countWords(tagList)
        tagTagDict, tagTagCountV, tagTagCountN=myUtil.countWords(tagTagList)
        wordTagDict, wordTagCountV, wordTagCountN = myUtil.countWords(wordTagList)
        
        #debug
        print("wordTagCountV = {}".format(wordTagCountV))
        print("tagCountV = {}".format(tagCountV))
        print("tagTagCountV = {}".format(tagTagCountV))
        # debug -ends

        
        
        
        
        


        
# |---------------------------------myUI---------------------------------------|
    





if __name__ == '__main__':
    inFile =  sys.argv[1]
    posTaggingUI = POSTaggingUI()
    posTaggingUI.myUI(inFile)