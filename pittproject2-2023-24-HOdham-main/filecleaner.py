#hendrix odham 
def processFile(fname):# cleans the file
    words = []
    try:
        file = open(fname, 'r', encoding='utf-8')
        for line in file:
            for word in line.split(): #by default it splits at spaces or tabs
                cleanedWord = '' # cleaned word
                for char in word: # checks the chars in the returned word from the array from line.split
                    if char.isalpha():
                        cleanedWord += char
                cleanedWord = cleanedWord.lower()
                if cleanedWord: # if the cleaned word has something in it 
                    words.append(cleanedWord)
    except FileNotFoundError as fnf_error: # execption for the file not being found
        print(f"File not found error: {fnf_error}")
    except Exception as e:
        print(f"An error occurred while processing the file '{fname}': {e}") # any other errors thrown
    finally: # closing the file even if an exception was thrown
        if file:
            file.close()
    return words

def countWords(tokens): # this function counts all the words inside of the book and puts it in a dict this uses process file
    wordCounts = {} #init dict
    for token in tokens: # loop through the list
        if token in wordCounts: # if the token is already there then add 1
            wordCounts[token] += 1
        else:
            wordCounts[token] = 1 # if its not there then set it to 1
    return wordCounts #returned dict needed for the top func

def top(tokens, k): # find the top words
    wordCounts = tokens #this orgianly called another function so thats why i created a new var
    topWords = {} #new dict to return
    for n in range(k): # i like to use _ if im not using the var
        maxCount = 0 # counter
        maxWord = None # init var
        for word, count in wordCounts.items(): # word is the key count is the value [the] : 50
            if count > maxCount: # if the key is > than the max amount of the key found then finalize the count
                maxCount = count
                maxWord = word
        if maxWord is not None: # if the finalized word is something
            topWords[maxWord] = maxCount # put it in return dict
            del wordCounts[maxWord] # delete it so it does not get looped through again
    return topWords

def findUncommon(current, other1, other2): # does as said
    uncommonWords = {} # init dict
    for word in current.keys(): # go through the cleaned counted and toped file
        if word not in other1.keys() and word not in other2.keys(): # check if the word is not found in other1 and other 2 then its uncommon
            uncommonWords[word] = current[word] # add the uncommom word and its count to the dict
    return uncommonWords

def main():
    scarlet = top(countWords(processFile("scarlet.txt")), 250) # count was orginally called in the top function
    sign = top(countWords(processFile("sign.txt")), 250)
    hound = top(countWords(processFile("hound.txt")), 250)

    scarletUncommon = findUncommon(scarlet, sign, hound)
    signUncommon = findUncommon(sign, scarlet, hound)
    houndUncommon = findUncommon(hound, scarlet, sign)

    print("Uncommon words from 'A Study in Scarlet':", scarletUncommon, "\n")
    print("Uncommon words from 'The Sign of the Four':", signUncommon, "\n")
    print("Uncommon words from 'The Hound of the Baskervilles':", houndUncommon, "\n")

if __name__ == "__main__":
    main()
