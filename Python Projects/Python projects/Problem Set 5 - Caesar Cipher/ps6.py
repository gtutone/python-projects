import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                       'w', 'x', 'y', 'z']
        upperList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                     'Y', 'Z']
        # lowerDict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f',
        #              'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l',
        #              'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r',
        #              's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x',
        #              'y': 'y', 'z': 'z'}
        # upperDict = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F',
        #              'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
        #              'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
        #              'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        #              'Y': 'Y', 'Z': 'Z'}
        shiftDict = {}
        
        # iterate over lowercase list, add shift to index number and add to the shifted dictionary
        for i in range(len(lowerList)):

            if i+shift < 26:
                shiftDict[lowerList[i]] = lowerList[i+shift]
            # if the shift goes over length of alphabet, subtract 26 to start over
            else:
                shiftDict[lowerList[i]] = lowerList[i+shift-26]
         
                # iterate over uppercase list, add shift to index number and add to the shifted dictionary
        for i in range(len(upperList)):

            if i+shift < 26:
                shiftDict[upperList[i]] = upperList[i+shift]
            # if the shift goes over length of alphabet, subtract 26 to start over
            else:
                shiftDict[upperList[i]] = upperList[i+shift-26]

        
        return shiftDict
            
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        newMessage = ''
        cypher = self.build_shift_dict(shift)
        cypher[' '] = ' '
        
        # add punctuation
        for i in range(len(string.punctuation)):
            cypher[string.punctuation[i]] = string.punctuation[i]
        
        # add digits
        for i in range(len(string.digits)):
            cypher[string.digits[i]] = string.digits[i]
        
        # apply cypher to message
        for i in self.message_text:
            newMessage = newMessage + str(cypher[i])
        
        return newMessage
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        CopyEncryptingDict = self.encrypting_dict.copy()
        return CopyEncryptingDict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        splitText = []
        validWords = {}
        decrypted = ()
        # iterate over all possible shift values
        for i in range(26):
            ShiftedText = self.apply_shift(i)
            # Split the shifted text and add it to a list
            splitText = ShiftedText.split(' ')
            
            # Check how many words in the shifted text list are valid
            for word in splitText:
                # For each valid word, add shift# as key, and +1 as value to dict
                if is_word(self.valid_words, word):
                    validWords[i] = validWords.get(i, 0) + 1
                # If word is invalid, still add shift# as key and 0 as value
                else:
                    validWords[i] = validWords.get(i, 0)
        # Get best shift key
        values = list(validWords.values())
        keys = list(validWords.keys())
        bestKey = keys[values.index(max(values))]
        # Add best shift key to decrypted tuple and decode message        
        decrypted = (bestKey, self.apply_shift(bestKey))
        
        return decrypted
        
def decrypt_story():
    story = get_story_string()
    
    story = CiphertextMessage(story)
    
    return story.decrypt_message()






# Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 10)
print('Output:', plaintext.get_message_text_encrypted())
print(plaintext.get_encrypting_dict())
print(plaintext.shift)
plaintext.change_shift(15)
print(plaintext.shift)
print(plaintext.get_message_text_encrypted())
print(plaintext.get_encrypting_dict())
    
# # Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('jgnnq ciao')
# print('Expected Output:', (24, 'hello'))
# print('Actual Output:', ciphertext.decrypt_message())

# # Message class test case
# hello = Message("xyz 12345")
# print(hello.apply_shift(3))
    
# print(decrypt_story())