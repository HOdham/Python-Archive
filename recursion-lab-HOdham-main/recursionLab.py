#nice job 20/20

#Required Function
#Returns the user's choice as a string.
def validateRecursion(values):
    userInput = input(f"Choose from {values}: ")

    if userInput in values:
        return userInput
    elif userInput.isnumeric() and int(userInput) in values:
        return int(userInput)
        
    print(f"Invalid selection {userInput}. Please try again.")
    return validateRecursion(values)


#Returns the value of the 'number'th term in the sequence that starts with 1 and adds by 5
def arSequence(number):
    if number == 1:
        return 1
    else:
        return number + arSequence(number - 1)

#Returns the value of the 'number'th term in the series that starts with 3 and multiplies by 5
def geoSequence(number):
    if number == 1:
        return 3
    else:
        return 5 * geoSequence(number - 1)

#Returns the factorial of the number
def factoral(num):
    if num == 1:
        return 1
    else:
        return num * factoral(num - 1)

#Returns the gcd of the two numbers
def gcd(large, small):
    if small == 0:
        return large
    else:
        return gcd(small, large % small)

#Returns the nth term in the Fibonacci sequence
def fibSeq(nth):
    if nth <= 1:
        return nth
    else:
        return fibSeq(nth - 1) + fibSeq(nth - 2)

#Returns the sum of all numbers up to and including num
def summation(num):
    if num == 0:
        return 0
    else:
        return num + summation(num - 1)


