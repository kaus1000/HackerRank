import sys
inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]

for inputString in inputData:
    
    wordsString = inputString[4:]
    
    if inputString[0] == 'S':
        
        wordList = []
        word = ''
        
        wordsString += '('
        
        for i in range(len(wordsString)):
            word += wordsString[i]

            if wordsString[i+1].isupper():
                wordList.append(word)
                word = ''

            elif wordsString[i+1] == '(':
                wordList.append(word)
                break

        result = ' '.join(wordList).lower()
        

    else:
        wordList = wordsString.split(' ')
        if inputString[2] == 'C':
            wordList[0] = wordList[0].capitalize()
        for i in range(1, len(wordList)):
            wordList[i] = wordList[i].capitalize()

        result = ''.join(wordList)         
        if inputString[2] == 'M':
            result += '()'
    
    print(result)