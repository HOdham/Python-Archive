#overall very nice job.  A few minor syntax issues on formatName. See comments Below
#score 29/40

def getHypotenuse(a, b): 

    hypotenuse = ((a ** 2) + (b ** 2)) ** 0.5
    return f"{hypotenuse:.2f}"

def binaryConvert(num):
    binary = ""
    #exactly how it was shown in class could use a while loop for an number
    for _ in range(8):
        binary = str(num % 2) + binary
        num //= 2
    return binary

def getCapLetter():
    letter = input("Enter a capital letter: ")
    while not letter.isupper() or len(letter) != 1:
        letter = input("Enter a capital letter: ")
        
    return letter

def getLowerLetter():
    letter = input("Enter a lowercase letter: ")
    while not letter.islower() or len(letter) != 1:
        letter = input("Enter a lowercase letter: ")
    return letter

def getInteger():
    num = input("Enter an integer: ")
    while not num.isnumeric():
        num = input("Invalid Enter an integer: ")
    return int(num)

def getNum(a, b):
    num = input(f"Enter a number between {a} and {b}: ")
    while not (num.isnumeric() and a <= float(num) and float(num)<= b):
        num = input(f"Enter a number between {a} and {b}: ")
    return float(num)

def summation(*args):
    result = 0
    for number in args:
        result += number
    return result


    

def formatName(firstName, lastName = False,middleName= False): #type LastName was lastNam.. I fixed.
    if middleName:
        return f"{lastName[0].upper()+lastName[1:]}, {firstName}, {middleName[0].upper()}." #missed() on upper function.
    elif lastName:
        return f"{lastName}, {firstName}"
    else:
        return firstName

def findSomething(subString, aString):
    for i in range(len(aString)):
        if aString[i] == subString:
            return i
    return None

# Function Interface
if __name__ == "__main__":
    # Code block to execute when the script is run as the main program
    # Calls to the functions to demonstrate their functionality
    
    a, b = 3, 4 # vars for Hypotenuse
    hypotenuse = getHypotenuse(a, b) # run the function
    print(f"1. Hypotenuse: {hypotenuse}") # print the return value

    num = 132 # var for binary
    binary_num = binaryConvert(num) # run the function
    print(f"2. Binary Conversion: {binary_num}") # print the return value

    cap_letter = getCapLetter() # run the fucntion no args
    print(f"3. Capital Letter: {cap_letter}") # print return value

    lower_letter = getLowerLetter() # run the function
    print(f"4. Lowercase Letter: {lower_letter}") #print the return value

    integer = getInteger()
    print(f"5. Integer: {integer}")

    a, b = 1, 10
    number = getNum(a, b)
    print(f"6. Number between {a} and {b}: {number}")

    numbers = 1, 2, 3, 4, 5
    total = summation(*numbers)
    print(f"7. Summation: {total}")

    first_name, last_name, middle_name = "Hendrix", "Coal", "Odham"
    formatted_name = formatName(first_name, last_name, middle_name)
    print(f"8. Formatted Name: {formatted_name}")

    substring, phrase = "o", "Hello, World!"
    index = findSomething(substring, phrase)
    print(f"9. Index of '{substring}' in '{phrase}': {index}")
