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
        # debug
        print("biGramList = {}".format(biGramList))
        print("len(biGramList) = {}".format(len(biGramList)))
        # debug -ends


       
# |--------------------------------myNGramUI---------------------------------|
    















if __name__ == '__main__':
    inFile =  sys.argv[1]
    nGramUI = NGramUI()
    nGramUI.myNGramUI(inFile)