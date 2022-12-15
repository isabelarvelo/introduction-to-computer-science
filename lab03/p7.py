"""
This script utilizes functions from the module wordTools to solve the NPR puzzle
proposed on September 22, 2020:

Suppose you have a seven letter hive, ’mixcent’. How many 4-letter lowercase
words in ’words/dict’ (1) include ’m’ and (2) are spelled only using (possibly
repeated) letters from the hive string?
"""

from wordTools import *

hive = 'mixcent'

#creating a list of words from 'words/dict'
dictionary = sized(4,words('words/dict'))

fourHive = []

for word in dictionary:
    #only considering lowercase words that include 'm'
    if str('m') in word and word.islower():
        keep = True
        for letter in word:
            #eliminating words with letters not in hive
            if letter not in hive:
                keep = False
        if keep:
            fourHive.append(word)

count = len(fourHive)
print("There are {} words in 'words/dict' that meet these conditions.".format
    (count))
