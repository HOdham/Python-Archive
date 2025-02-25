import recursionLab as RL
import os

os.system('cls')

#Recursive Validation:
print(f'Recursive Validation \t You chose:\t{ RL.validateRecursion(("a","b",4,"9"))}\n')


num = 3

#Arithmetic Sequence (start at 1 add by 5) 1,6,11,16,21

print(f"The {num}th term in the Arithmetic Squene is:\t{RL.arSequence(num)}:\n")


#Geometric Sequence start at 3 multiples by 5 ex 3,15,75,375...
print(f"The {num}th term in the Geometric Sequence is:\t{RL.geoSequence(num)}:\n")


#Fibonacci Sequence.
print(f"The {num}th term in the Fibonacci Sequence is:\t{RL.fibSeq(num)}:\n")
 

#Factoral 
print(f"Factoral {num}! =\t{RL.factoral(num)}\n")


small = 42
large = 76
#GCD of a and b
print(f"The GCD of {small} and {large} is:\t {RL.gcd(large,small)}:\n")


#summation
print(f'The sum of all numbers up to {num} is:\t {RL.summation(num)}\n')



