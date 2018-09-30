import sys
from myUtil import MyUtil
class POSTaggingUI:

# |----------------------------------------------------------------------------|
# myUI
# |----------------------------------------------------------------------------|
    def myUI(self, inFile):
        '''
        
        '''
        myUtil = MyUtil()
        corpusList, tagList = myUtil.readPOSFile(inFile)


        
# |---------------------------------myUI---------------------------------------|
    




















if __name__ == '__main__':
    inFile =  sys.argv[1]
    posTaggingUI = POSTaggingUI()
    posTaggingUI.myUI(inFile)