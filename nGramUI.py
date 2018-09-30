import sys
from myUtil import MyUtil
from nGram import NGram
class NGramUI:
    
# |----------------------------------------------------------------------------|
# myNGramUI
# |----------------------------------------------------------------------------|
    def myNGramUI(self, inFile):
        '''
        Given function 
        1. reads file
        2. get unigram and bigram counts
        3. apply smoothing functions to compute bigram models for
            a. No Smoothing
            b. Add-one smoothing
            c. Good Turing Discounting based smoothing
        4. write these model into respective output files
        '''
        #1. read file
        myUtil = MyUtil()
        strList = myUtil.readFile(inFile)
        
        
        #get unigram and bigrams
        nGram = NGram()
        #create bigram
        biGramList = nGram.createBiGram(strList)

        #get unigram and bigram counts
        uniGramDict, uniGramCountV, unigramCountN=nGram.countWords(strList)
        biGramDict, biGramCountV, bigramCountN = nGram.countWords(biGramList)

        probDict = nGram.noSmoothing(biGramList, uniGramDict, biGramDict)
        # debug
        print("probDict =\n{}".format(probDict))
        print("uniGramCountV = {}".format(uniGramCountV))
        print("biGramCountV = {}".format(biGramCountV))
        print("biGramCountN = {}".format(bigramCountN))
        # debug -ends
        outFile = "no_smoothing_prob.txt"
        outFlag = myUtil.writeProbability(probDict, outFile)
        print(outFlag)



# |--------------------------------myNGramUI---------------------------------|
    















if __name__ == '__main__':
    inFile =  sys.argv[1]
    nGramUI = NGramUI()
    nGramUI.myNGramUI(inFile)