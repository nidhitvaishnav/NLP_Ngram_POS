import sys
from myUtil import MyUtil
from nGram import NGram
class POSTaggingUI:

# |----------------------------------------------------------------------------|
# myUI
# |----------------------------------------------------------------------------|
    def myUI(self, inFile):
        '''
        
        '''
        myUtil = MyUtil()
        corpusList, tagList, lineList = myUtil.readPOSFile(inFile)
        
        
        
        


        
# |---------------------------------myUI---------------------------------------|
    




















if __name__ == '__main__':
    inFile =  sys.argv[1]
    posTaggingUI = POSTaggingUI()
    posTaggingUI.myUI(inFile)