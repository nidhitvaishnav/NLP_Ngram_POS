# NLP_Ngram_POS
Given NLP project applies NGram algorithms like No - smoothing, Add-one Smoothing, Good- Turing Discounting and smoothing and Transformation based POS tagging such as Brill's transformation based POS tagging and Naive Bayesian classification tagging.

- For the implimentation of all codes, python 3.6 has been used.

### Script instructions:
##### nGramUI.py	:- 
  which contains the wrapper function of Q-2 and it performs no smoothing, add 1 smoothing and good turing discounting based solution
##### nGram.py	:- 
  It contains all the functions details related to Bigram probability model
##### POSTaggingUI.py:-
  It contains the wrapper function of Q-3 and performs brills transformation and naive bayes classification based POS tagging
#####  POS_Tagging.py:- 
  It contains all the function details related to transformation based POS Tagging
##### myUtil.py	:-
  It contains utility operations like file I/O, data pre-processing etc.
  
- To run bigram functions, like probability without smoothing, probability with add one smoothing and good turing, good turing with discounting
run nGramUI.py on command line with input file as other argument:
python nGramUI.py [InputfileName]
Ex.
python nGramUI.py nGramCorpus.txt

### Execution instruction:-

- To run Transformation based Part Of Speech tagging functions, like naive bayes transformation or brill's algorithm, run POSTaggingUI.py  on command line with input file as other argument:
python POSTaggingUI.py [InputFileName]
Ex.
python POSTaggingUI.py POS_Tags.txt
