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
        wordList, tagList, wordTagList, lineList = myUtil.readPOSFile(inFile)
        
        pos_Tagging = POS_Tagging()
        tagTagList = pos_Tagging.createTagTagList(wordTagList)
        # debug
        print("len(wordTagList = {}, tagTagList = {}".format(len(wordTagList), len(tagTagList)))
        # debug -ends

        #get unigram and bigram counts
        tagDict, tagCountV, tagCountN = myUtil.countWords(tagList)
        tagTagDict, tagTagCountV, tagTagCountN=myUtil.countWords(tagTagList)
        wordTagDict, wordTagCountV, wordTagCountN = myUtil.countWords(wordTagList)

        probWTDict, probTTDict  = pos_Tagging.naiveBayesClassification(wordTagList, tagDict,\
                                                     wordTagDict, tagTagDict)
#         # debug
#         print("probDict = {}".format(probWTDict))
#         # debug -ends
        outFile = "naive_Bayes_WT_Prob.txt"
#         outFlag = myUtil.writeCStarProbability(probDict, wordTagList, outFile)
        outFlag = myUtil.writeCStarProbability(probWTDict, wordTagDict, outFile)
        outFile = "naive_Bayes_TPrevT_Prob.txt"
        outFlag = myUtil.writeCStarProbability(probTTDict, tagTagDict, outFile)
#         # debug
#         print("probTTDict = {}".format(probTTDict))
#         # debug -ends
        brillsRule, mostProbablePOS  = pos_Tagging.brillsPOSTagging(wordList, tagList)
        #write rules
        outFile = 'brillsTags.txt'
        myUtil.writeBrillsRuleFile(brillsRule, outFile)
        input = "The_DT president_NN wants_VBZ to_TO control_VB the_DT board_NN 's_POS control_NN"
        pos_Tagging.applyBrillsRules(input, mostProbablePOS, brillsRule)

        
# |---------------------------------myUI---------------------------------------|
    





if __name__ == '__main__':
    inFile =  sys.argv[1]
    posTaggingUI = POSTaggingUI()
    posTaggingUI.myUI(inFile)
    