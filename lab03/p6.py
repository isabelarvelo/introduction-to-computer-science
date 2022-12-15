"""
This script utilizes functions from the module wordTools to count how many
lowercase 7-letter isograms in the word list 'words/dict'
"""
from wordTools import *


#create a list of seven letter words in 'words/dict'
dict = sized(7, words('words/dict'))

result = []

for word in dict:
    if isIsogram(word) and word.islower():
        result.append(word)
        #count the number of words in the list of isograms
        count = len(result)

print("There are {} lowercase 7-letter isograms in 'words/dict'.".format(count))
