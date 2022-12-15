#******************************************************************************
# Task 2: bedtimeStory (fruitful)
# Produces a recursive bedtime story based on a set of characters passed in
# as command line arguents.
#******************************************************************************

#base case talk through general approach - how to use functions
def bedtimeStory(characters):
    """
    Main (recursive) method for producing a bedtime story based on a list of
    characters passed in as a list of strings.

    >>> bedtimeStory(['ant'])
    ''
    >>> bedtimeStory(['ant', 'fly'])
    "So the ant's mother told them a story to fall asleep about a fly... \\n\\nand then the ant fell asleep."
    >>> bedtimeStory(['shrimp', 'salmon', 'trout', 'lobster'])[190:260]
    'o fall asleep about a lobster... \\n\\nand then the trout fell asleep.\\nand'
    """
    #base case
    if not characters[1:]:
    #cannot tell the story with one character so return empty line
        return "\n"
    else: #peel back first and last sentence to end up with middle of story
        return firstSentence(characters[0], characters[1]) + bedtimeStory(characters[1:]) +lastSentence(characters[0])
    #similar to the structure of a nested Russian doll

    #temporarily shortenning characters with indexing, but not popping off
    #because we don't want to mutate the original list

def firstSentence(subject, object):
    """returns a sentence about a subject's mother telling them a story about
    the object (in linguistics terms!)"""
    return "So the {}'s mother told them a story to fall asleep about a {}...\n".format(subject,object)

def lastSentence(subject):
    """ returns the second sentence for the specific character"""
    return  "and then the {} fell asleep.\n".format(subject)


if __name__ == "__main__": #give this
#was told that we can ignore doc test
    from doctest import testmod
    testmod()
    from sys import argv
    print(bedtimeStory(argv[1:]))
