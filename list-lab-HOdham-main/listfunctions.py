def makeCopy(lst):
    newList = []
    for item in lst:
        newList.append(item)
    return newList

def makeAnotherCopy(lst):
    newList = []
    i = 0
    while i < len(lst):
        newList.append(lst[i])
        i += 1
    return newList

def calculateAverage(lst):
    total = 0
    for num in lst:
        total += num
    average = total / len(lst)
    return average

def findMinimum(lst):
    minVal = lst[0]
    minIndex = 0
    for i in range(1, len(lst)):
        if lst[i] < minVal:
            minVal = lst[i]
            minIndex = i
    return minVal, minIndex

def combineLists(list1, list2):
    combinedList = []
    for i in range(len(list1)):
        combinedList.append(list1[i])
        combinedList.append(list2[i])
    return combinedList

def reverseOrder(lst):
    reversedList = []
    for i in range(len(lst) - 1, -1, -1):
        reversedList.append(lst[i])
    return reversedList

def removeAtIndex(lst, index):
    newList = []
    for i in range(len(lst)):
        if i != index:
            newList.append(lst[i])
    return newList



if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'Seven', 'Eight', 'nine', 'ten']

    copiedList1 = makeCopy(list1)
    print("Copy using for loop:", copiedList1)

    copiedList2 = makeAnotherCopy(list2)
    print("Copy using while loop:", copiedList2)

    avg = calculateAverage(list1)
    print("Average of list1:", avg)

    minVal, minIndex = findMinimum(list2)
    print("Minimum value and index in list2:", minVal, minIndex)

    combined = combineLists(list1, list2)
    print("Combined list:", combined)

    reversedList1 = reverseOrder(list1)
    print("Reversed list1:", reversedList1)

    indexToRemove = 3
    newList1 = removeAtIndex(list1, indexToRemove)
    print("List1 with item at index {} removed:".format(indexToRemove), newList1)
