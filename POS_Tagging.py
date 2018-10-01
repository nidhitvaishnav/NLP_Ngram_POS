from collections import Counter
from myUtil import MyUtil
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

        probTagTagDict = self._getTagTagDictProbability(tagDict, tagTagDict)
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
    def _getTagTagDictProbability(self,tagDict, tagTagDict):
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

# |----------------------------------------------------------------------------|
# brillsPOSTagging
# |----------------------------------------------------------------------------|
    def brillsPOSTagging(self, wordList, tagList):
        '''
        
        '''
        unigrams = self._createUnigrams(wordList, tagList)
        mostProbablePOS, modTags = self._mostProbablePOS(unigrams, wordList)
        uniqueTags = ['NN', 'VB']
        brillsRule = self._brillsPOS(tagList, modTags, uniqueTags)
        return brillsRule, mostProbablePOS
        
# |--------------------------------brillsPOSTagging---------------------------------|
# |----------------------------------------------------------------------------|
# createUnigrams
# |----------------------------------------------------------------------------|
    def _createUnigrams(self, wordList, tagList):
        '''
        
        '''
        tokenTags = {}
    
        for i in range(len(wordList)):
            if not wordList[i] in tokenTags:
                tokenTags[wordList[i]] = [tagList[i]]
            else:
                tokenTags[wordList[i]].append(tagList[i])
    
        return tokenTags
        
# |--------------------------------createUnigrams---------------------------------|

# |----------------------------------------------------------------------------|
# mostProbablePOS
# |----------------------------------------------------------------------------|
    def _mostProbablePOS(self, unigramDict, wordList):
        '''
        
        '''
        modTags = []
        for key, value in unigramDict.items():
            counter = Counter(value)
            maxValue = counter.most_common()[0]
            unigramDict[key] = maxValue[0]
    
        for word in wordList:
            modTags.append(unigramDict[word])
    
        return unigramDict, modTags
        
# |--------------------------------mostProbablePOS---------------------------------|
# |----------------------------------------------------------------------------|
# brillsPOS
# |----------------------------------------------------------------------------|
    def _brillsPOS(self, tags, mostProbableTags, uniqueTags):
        '''
        
        '''
        brillsTemplate = {}
        modTags = mostProbableTags[:]
    
        for index in range(1,8):
            threshold = 0
            print('Rule ', index)
            for fromTag in uniqueTags:
                for toTag in uniqueTags:
                    brillsRuleDictionary = {}
    
                    if fromTag == toTag:
                        continue
    
                    for pos in range(1, len(modTags)):
                        if tags[pos] == toTag and modTags[pos] == fromTag:
    
                            # rule = (PREVIOUS_TAG, FROM, TO)
                            rule = (modTags[pos - 1], fromTag, toTag)
                            if rule in brillsRuleDictionary:
                                brillsRuleDictionary[rule] += 1
                            else:
                                brillsRuleDictionary[rule] = 1
    
                        elif tags[pos] == fromTag and modTags[pos] == fromTag:
    
                            rule = (modTags[pos - 1], fromTag, toTag)
                            if rule in brillsRuleDictionary:
                                brillsRuleDictionary[rule] -= 1
                            else:
                                brillsRuleDictionary[rule] = -1
    
                    if brillsRuleDictionary:
                        maxValueKey = max(brillsRuleDictionary, key=brillsRuleDictionary.get)
                        maxValue = brillsRuleDictionary.get(maxValueKey)
    
                        if maxValue > threshold:
                            threshold = maxValue
                            tupel = maxValueKey
    
            for i in range(len(modTags) - 1):
                if modTags[i] == tupel[0] and modTags[i + 1] == tupel[1]:
                    modTags[i + 1] = tupel[2]
    
            brillsTemplate[tupel] = threshold
    
        sortedBrillsTemplate = sorted(brillsTemplate.items(), key=lambda x: x[1], reverse=True)
    
        return sortedBrillsTemplate
        
# |--------------------------------brillsPOS---------------------------------|
# |----------------------------------------------------------------------------|
# applyBrillsRules
# |----------------------------------------------------------------------------|
    def applyBrillsRules(self, input, mostProbablePOS, brillsRule):
        '''
        
        '''
        # input = sys.argv[1]
        inputList = []
        inputTokens = []
        inputGoldTags = []
        inputMostProbable = []
        mostProbableErrorIndex = []
        brillRuleErrorIndex = []
        mostProbableError = 0
        brillRuleError = 0
    
        for i in range(len(input.split())):
            if i < (len(input.split()) - 1):
                inputList.append((input.split()[i], input.split()[i + 1]))
            inputTokens.append(input.split()[i].split('_')[0])
            inputGoldTags.append(input.split()[i].split('_')[1])
    
        for i in range(len(inputTokens)):
            inputMostProbable.append(mostProbablePOS[inputTokens[i]])
    
        inputBrills = inputMostProbable[:]
    
        for i in range(len(inputMostProbable) - 1):
            for k, v in brillsRule:
                prev = k[0]
                frm = k[1]
                to = k[2]
    
                if inputBrills[i] == prev and inputBrills[i + 1] == frm:
                    inputBrills[i + 1] = to
                    brillRuleErrorIndex.append(i + 1)
                    break
    
        for i in range(len(inputGoldTags)):
            if (inputGoldTags[i] != inputMostProbable[i]):
                mostProbableErrorIndex.append(i)
                mostProbableError += 1
            if (inputGoldTags[i] != inputBrills[i]):
                brillRuleError += 1
    
        print('\n')
    
        print('Most Probable Tag Error Rate: ', mostProbableError / len(inputGoldTags))
        print('Brills Tag Error Rate: ', brillRuleError / len(inputGoldTags))

# |--------------------------------applyBrillsRules---------------------------------|
    
