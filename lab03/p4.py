#from strings import rotate
from wordTools import *

#creating a list of words from file
diseases = words('words/diseases')
bibleNames = words('words/bibleNames')

#creating a list of 5-letter diseases
fiveDisease = sized(5,diseases)

result = []

for disease in fiveDisease:
    #shift each letter in disease three spaces later in the alphabet
    affliction =rotate(disease, 3)
    if affliction in bibleNames:
        print("The prominenet bible name is {}.".format(affliction))
