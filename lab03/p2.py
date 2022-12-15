"""
This script utilizes functions from the module wordTools to solve the NPR puzzle
proposed on August 16, 2020:

Think of a major city in France whose name is an anagram of a major
city in Italy. What cities are they?
"""

from wordTools import *

#creating a list of words from file
frenchCities = words('words/frenchCities')
italianCities = words('words/italianCities')

for fCity in frenchCities:
    frenchLength=len(fCity)
    #return a canonical version of French city
    fcanon = canon(fCity)
    #look for Italian cities with same number of letters as French cities
    samelen = sized(frenchLength, italianCities)
    for iCity in samelen:
        icanon = canon(iCity)
        #anagrams will have the same canonical version of words
        if icanon == fcanon:
            print ("{} is an anagram of {}.".format(fCity, iCity))
