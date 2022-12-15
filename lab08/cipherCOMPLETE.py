"""The basis for building objects that can encode and decode messages.

   Typical usage:
   >>> coder = CaesarCipher(7)  # any particular cipher
   >>> coder.encode('Hello, world.')
   'OLSSVDVYSK'
   >>> coder.decode('OLSSVDVYSK')
   'HELLOWORLD'
"""
__all__ = [ 'CaesarCipher', 'Cipher', 'Rot13', 'Vigenere' ]


class Cipher(object):
    """The base class/interface for all Cipher classes."""

    __slots__ = []

    def __init__(self):
        """Trivial base class initialization."""
        pass

    def encode(self,sourceString):
        """Placeholder for encode method in subclasses."""
        return sourceString

    def decode(self,sourceString):
        """Placeholder for encode method in subclasses."""
        return sourceString

    # here down: private utility methods, available to subclasses:
    def _normalize(self,sourceString):
        """Normalize by eliminating non-letters, then upper-casing.
        >>> coder = Cipher()
        >>> coder._normalize('Hello, world.')
        'HELLOWORLD'
        """
        return ''.join([c.upper() for c in sourceString if c.isalpha()])

    def _a2i(self,a):
        assert a.isalpha() and len(a) == 1
        return (ord(a) & 31)-1

    def _i2a(self,i):
        return 'abcdefghijklmnopqrstuvwxyz'[i%26]

    def _i2A(self,i):
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i%26]

    def _rotate(self, c, n):
        """Rotate letters n steps around alphabet; other chars unchanged.

        >>> coder = Cipher()
        >>> coder._rotate('m',4)
        'q'
        >>> coder._rotate('!',4)
        '!'
        """
        assert len(c) == 1
        if c.isalpha():
            newCode = (self._a2i(c)+n)%26
            c = self._i2a(newCode) if c.islower() else self._i2A(newCode)
        return c

    def __str__(self):
        """Convert cipher to a string."""
        return "<a simple cipher>"

    def __repr__(self):
        """Generate representation of Cipher."""
        return "Cipher()"

class CaesarCipher(Cipher):
    """Encode messages using rotation by n alphabetic characters."""

    __slots__ = ['_n']

    def __init__(self,n):
        """Construct a rotation-by-n encode/decode."""
        super().__init__()
        self._n = n%26

    def encode(self,sourceString):
        """Encode by rotating characters of sourceString forward
        by a constant."""
        coded = ''
        for c in self._normalize(sourceString):
            coded += self._rotate(c,self._n)  # encoding: map forward
        return coded

    def decode(self,sourceString):
        """Decode by rotating characters of sourceString backward by a constant.

        >>> coder = CaesarCipher(15)
        >>> plaintext = coder.decode(open('story.txt').read())
        >>> plaintext.count('AMHERST')
        4
        """
        coded = ''
        for c in self._normalize(sourceString):
            coded += self._rotate(c,-self._n) # decoding: map backward
        return coded

    def __repr__(self):
        """Representation of the CaesarCipher."""
        return "CaesarCipher({})".format(n)

class Rot13(CaesarCipher):
    """Subclass of CaesarCipher(n) with a fixed value of n, 13."""

    __slots__ = []

    def __init__(self):
        """Construct a rotation-by-13 encode/decode.

        >>> code = open('reform.txt').read()[:46]
        >>> coder = Rot13()
        >>> plain = coder.decode(code)
        >>> plain == 'A Plan for the Improvement of English Spelling'
        True
        >>> code = 'Uv V whfg ngr 7 pbbxvrf & 2 fpbarf!'
        >>> coder = Rot13()
        >>> confession = coder.encode(code)
        >>> confession == 'Hi I just ate 7 cookies & 2 scones!'
        True
        """

        #hardcoding initializer with a fixed value of n=13
        super().__init__(13)


    def _normalize(self,sourceString):
        """Normalize by eliminating non-letters, then upper-casing.
        >>> coder = Rot13()
        >>> coder._normalize('Hello, world.')
        'Hello, world.'
        """
        #return input sourceString so that punctuation and case remain the same
        #this is useful for obfuscation
        return sourceString

    def __repr__(self):
        """Representation of the Rot13 CaesarCipher"""
        return "Rot13()"

class Vigenere(Cipher):
    """Encode messages using a simple form of polyalphabetic substitution by
    rotating letters using alphabet code of key"""

    slots = ['_key']

    def __init__(self,key):
        """Extend Cipher Class and construct a normalized key
        >>> vCoder = Vigenere('Ilove.Pandas')
        >>> vCoder._key
        'ILOVEPANDAS'
        """
        super().__init__()

        #normalize key
        #need to call self._normalize because it is a method of the class
        self._key = self._normalize(key)

    def encode(self,sourceString):
        """Encode by rotating letters using alphabet code of the key.
        >>> vCoder = Vigenere('Williams')
        >>> vCoder.encode('purple cows')
        'LCCATEOGSA'
        """
        coded = ''
        #create a variable for normalized Source String to make code cleaner
        #since it will be referred to several times
        ss = self._normalize(sourceString)

        #iterating across values
        for i in range(0, len(ss)):
            #Index of key changes each time so it is defined within the for loop
            #Using mod operator allows us to use key even when it is shorter
            #than the sourcestring
            keyIndex = i%len(self._key)
            #use class method _a2i to abstract details of convertnig key to
            #alphabet code
            coded += self._rotate(ss[i],self._a2i(self._key[keyIndex]))

        return coded

    def decode(self,sourceString):
        """Decode by rotating characters of sourceString backward by a constant.

        >>> vCoder = Vigenere('Williams')
        >>> vCoder.decode('lccateogsa')
        'PURPLECOWS'
        >>> code = open('cia.txt').read()[:51]
        >>> coder = Vigenere('SANBORN')
        >>> coder.decode(code)
        'SANBORNSKRYPTOSISASCULPTURELOCATEDONTHEGROUNDSOFCIA'
        """
        #same process as encode but rotating letters backward in the alphabet
        coded = ''

        ss = self._normalize(sourceString)
        for i in range(0, len(ss)):
            keyIndex = i%len(self._key)
            # shifts backward by negating amount it shifted forward with encode
            coded += self._rotate(ss[i],-self._a2i(self._key[keyIndex]))

        return coded

    def __repr__(self):
        """Representation of the Vigenere Cipher"""
        return "Vigenere({})".format(self.key)


def test():
    """Perform doctests."""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test()
    coder = CaesarCipher(7) # use other ciphers!
    coder = Rot13()
    coder = Vigenere('Williams')
    encoding = coder.encode('Hello, world')
    decoding = coder.decode(encoding)
    print(decoding)
