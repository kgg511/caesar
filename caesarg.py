choice = ''
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()


def encrypt():
    initialWord = ''
    key = ''
    numbers = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'.split()
    while key not in numbers:
        print('How many letters would you like to shift the alphabet?')
        key = input()
    key = int(key)
    wordNum = ''
    while wordNum != 'one' and wordNum != 'multiple':
        print('Is it one word or mutliple? (one/multiple)')
        wordNum = input().lower()
    if wordNum == 'one':
        while not initialWord.isalpha():
            print('What word would you like to encrypt?')
            initialWord = input()
    else:
        while not initialWord.isalpha() and ' ' not in initialWord:
        #multiple words. Test for spaces
            print('What words would you like to encrypt?')
            initialWord = input()
    mLetters = list(alphabet[:key])
    shiftedAlphabet = alphabet.copy()
    del shiftedAlphabet[:key]
    shiftedAlphabet = shiftedAlphabet + mLetters
    for i in range(len(initialWord)):
        #find out what index an itme in one string is in another list
        if initialWord[i] == ' ':
            x = 1
        else:
            indexA = alphabet.index(initialWord[i])
            initialWord = list(initialWord)
            initialWord[i] = shiftedAlphabet[indexA]
    print('Your encrypted word/s: ' + ''.join(initialWord))





def decrypt():
    encryptedWord = ''
    key = ''
    numbers = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'.split()
    wordNum = ''
    while key not in numbers:
        print('What is the key? (The number of letters the alphabet shifted)')
        key = input()
    key = int(key)
    while wordNum != 'one' and wordNum != 'multiple':
        print('Is it one word or multiple? (one/multiple)')
        wordNum = input().lower()
    if wordNum == 'one':
        while not encryptedWord.isalpha():
            print('What word would you like to decrypt?')
            encryptedWord = input()
    else:
        while not encryptedWord.isalpha() and ' ' not in encryptedWord:
        #multiple words. Test for spaces
            print('What words would you like to decrypt?')
            encryptedWord = input()
    #to make the shifted alphabet
    mLetters = list(alphabet[:key])
    shiftedAlphabet = alphabet.copy()
    del shiftedAlphabet[:key]
    shiftedAlphabet = shiftedAlphabet + mLetters
    #now to do the actual decrypting
    for i in range(len(encryptedWord)):
        if encryptedWord[i] == ' ':
            x = 1
        else:
            #find
            indexS = shiftedAlphabet.index(encryptedWord[i])
            encryptedWord = list(encryptedWord)
            encryptedWord[i] = alphabet[indexS]
    print('Your decrypted word: ' + ''.join(encryptedWord))


while choice != 'encrypt' and choice != 'decrypt':
    print('Would you like to encrypt or decrypt a word with a caesar cipher?')
    choice = input().lower()
    if choice == 'encrypt':
        encrypt()
    if choice == 'decrypt':
        decrypt()






