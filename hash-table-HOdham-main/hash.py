#nice job 25/25
#please include a headere in your code with your name, date and period.

def bHash(word):
    N = 17
    M = 101

    asciiSum = 0
    for char in word:
        asciiSum += ord(char)

    hashedValue = (asciiSum * N) % M
    return hashedValue

def locate(hashTable, word):
    hashValue = bHash(word)

    if hashTable[hashValue] == -1:
        return -1

    index = hashValue
    while hashTable[index] != -1:
        if hashTable[index] == word:
            return word, index
        index = (index + 1) % M

        if index == hashValue:
            return -1

    return -1

def experimentHashing(words):
    M = 101
    hashTable = [-1] * M 

    for word in words:
        hashValue = bHash(word)

        while hashTable[hashValue] != -1:
            hashValue = (hashValue + 1) % M

        hashTable[hashValue] = word

    for i in range(0, M, 10):
        row = hashTable[i:i + 10]
        for val in row:
            if val != -1:
                print(str(val), end=" ")
            else:
                print("--", end=" ")
        print()

    wordToSearch = "dad"
    result = locate(hashTable, wordToSearch)

    if result != -1:
        print(f"The word '{result[0]}' is located at index {result[1]}.")
    else:
        print(f"The word '{wordToSearch}' does not exist in the hash table.")

wordsToHash = ["bob", "obb", "dad", "add", "dan", "and"]
experimentHashing(wordsToHash)

    