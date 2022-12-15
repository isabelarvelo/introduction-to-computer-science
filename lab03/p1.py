"""
This script utilizes functions from the module wordTools to solve the NPR puzzle
proposed on February 11, 2018:

Name part of the human body in six letters. Add an `r' and rearrange the result
to name a part of the body in seven letters. What is it?
"""
from wordTools import *

#list of human body parts with six letters
bodyParts = sized(6, words('words/bodyParts'))

#add 'r' to all body parts
bodyPartsR = [part + "r" for part in bodyParts]
#only considering body parts with seven letters
realBodyParts = sized(7, words('words/bodyParts'))

#comparing canonical version of words in bodyPartsR and realBodyParts to see if
#they are anagrams
for rPart in bodyPartsR:
    partRCanon = canon(rPart)
    for part in realBodyParts:
        partCanon = canon(part)
        if partCanon == partRCanon:
            print ("{} can be rearranged to spell {}.".format(rPart.capitalize()
            , part))
