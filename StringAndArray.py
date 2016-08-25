'''
This file contains attempts and solutions to the Arrays and Strings Chapter 
of coding practice.
'''

'''Problem: Implement an algorithm to determine if a string has all unique characters. What if you 
cannot use additional data structures.

My solution: Use a 26 char array and when we encounter a char mark it in the array. That way 
we can see which char we have encountered already. This should run in O(n) as we loop through the
array at most once. Note if we stick to the alphabet then we assume a - z if we assume 16 bit ascii
then our array has to be 255 bits'''
def Ernesto_unique_string(uniqueString):
    #make a 26 char array 
    uniqueString = uniqueString.lower()
    arr = [i for i in range(26)]
    #loop through string
    #ord(a) is 97
    for i in range(len(uniqueString)):
        index = ord(uniqueString[i]) - 97
        if arr[index] == 1:
            return False
        elif arr[index] == 0:
            arr[index] = 1
    return True

'''Problem: Given two strings, write a method to decide if one is a permutation of the other.

My solution: There's two ways that I can think of doing this the first is sorting the two strings and
then see if the characters match however this would be inefficient as we add the sorting algorithm
time into our runtime. The other solution I have is to map characters as a bit array and check if the arrays
match which should run in O(n) time.'''

def Ernesto_permutation(string1, string2):
    #small optimization test if the strings are equal length
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        return False
    arr1 = [0] * 26
    arr2 = [0] * 26
    for i in range(len(string1)):
        index1 = ord(string1[i]) - 97
        index2 = ord(string2[i]) - 97
        arr1[index1] += 1
        arr2[index2] += 1
    #now just do a set intersection and check the length
    result = set(arr1).intersection(arr2)
    #if we have the same number of matches then its a permutation
    return result == len(string1)

def main():
    print("Running tests on the unique string solution")
    print("Using Hello: {0}".format(Ernesto_unique_string("Hello")))
    print("Using basketball: {0}".format(Ernesto_unique_string("basketball")))
    print("Using unique: {0}".format(Ernesto_unique_string("unique")))

main()