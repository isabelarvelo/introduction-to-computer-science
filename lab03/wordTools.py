"""
A module of tools for manipulating words and word lists to solve puzzles.
"""

__all__ = [ "words", "sized", "canon", "isIsogram", "rotate"]


def words(filename):
    """Opens and reads words found in a file named with the string filename,
    returns the resulting list.

    >>> words('words/dict')[161131]
    'python'
    >>> words('words/bodyParts')[124]
    'pelvis'
    """
    results = []
    with open(filename) as wordFile:
        for line in wordFile:
            linewords = line.split()
            #splits line by white space so if there are multiple words on the
            #same line they will be read in as three separate names- could be
            #improved by splitting by '/n'
            results.extend(linewords)
    return results

def sized(n,wordList):
    """Returns a list of all the words in a list of words that are exactly
       length n.

    >>> sized(11,words('words/bodyParts'))
    ['circulatory', 'gallbladder', 'respiratory']

    >>> sized(20,words('words/places'))
    []

    >>> len(sized(6,words('words/bibleNames')))
    519
    """
    results = []

    for word in wordList:
        if len(word) == n:
            results.append(word)
    return results

def canon(word):
    """Returns a canonical version of word:
       * lower case letters
       * in alphabetical order
       * no spaces

    >>> canon('Mia')
    'aim'
    >>> canon('iAm')
    'aim'
    >>> canon('a lot')
    'alot'
    """
    #convert to lowercase
    result = word.lower()
    #sort letters into alphabetical order
    result = ''.join(sorted(result))
    #split by white space and join letters into string
    result = ''.join(result.split())

    return result

def isIsogram(word):
    """Returns true if the letters of the word are unique.

    >>> isIsogram('Unique')
    False
    >>> isIsogram('python')
    True
    """
    #convert to lowercase so uppercase and lowercase forms are read as the same
    word = word.lower()
    unique = []
    #comparing each letter in the word to the remaining letters in the word
    for i in range(len(word)):
        for j in range(i +1, len(word)):
            if word[i]== word[j]:
                return False
    return True


lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = lowers.upper()

def rotate(s,n=13):
    """Take the letters of the string s and rotate them n positions in
    the alphabet.

    >>> rotate('HAL',1)
    'IBM'
    >>> rotate('VMS',1)
    'WNT'
    """
    result = ''
    for c in s:
        if c in lowers:
            code = lowers.index(c)  # alphabet code for c
            code = (code + n)%26
            c = lowers[code]
        elif c in uppers:
            code = uppers.index(c)  # alphabet code for c
            code = (code + n)%26
            c = uppers[code]
        result += c
    return result

if __name__ == '__main__':
    # The following code is executed when you run wordTools as a script:
    # Tests will fail in this starter code.
    # As your work progresses, this module will pass more tests.
    from doctest import testmod
    testmod()  # test this module, according to the doctests
