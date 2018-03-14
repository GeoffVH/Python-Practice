# Simple coding questions found from different online sources that I answered for practice.


#///////////////////////////////////////////////////////////////////#
#Given a variable list of numbers, find the second most repeated digit.
import collections

inputList = list(map(int, input("Enter digits: ").split()))
inputCounter = collections.Counter(inputList)
print(inputCounter.most_common(2), " is the second most repeated digit.")


#///////////////////////////////////////////////////////////////////#
#Take a user input string and count the number of vowels. Include y as a vowel.
#Input can include uppercase characters. 
#>> I considered using counter, but it ended up neither shorter or more readable.
count = 0
for char in input("Enter the string: ").lower():
    if char in "aouiey": 
        count += 1
print(count, " is the amount of vowls in the given string")

#>>> After learning more on if conditions inside loop comprehensions I found a better way.
inputList = input("Enter the string: ").lower()
listOfVowls = [c for c in inputList if c in "aouiey"]
print(len(listOfVowls), " is the amount of vowls in the given string")


#///////////////////////////////////////////////////////////////////#
#Given a user-input digit, print the sum of it's individual digits. 
#E.G. 224 = 2+2+4 = 8
inputList = [int(char) for char in input("Enter the number: ")]
answer = 0
for num in inputList:
    answer += num
print(answer, " is the sum of all digits.")


#///////////////////////////////////////////////////////////////////#
#Reverse a given string.
inputString = input("Enter the string: ")
print(inputString[::-1])


#///////////////////////////////////////////////////////////////////#
#Given a user input string, remove all non-alphabetical characters
inputString = [i for i in input("Enter string: ") if i.isalpha() or i.isspace()]
answer = ''.join(inputString)
print(answer)


#///////////////////////////////////////////////////////////////////#
#Find the minimum of a variable amount of entries. 
num = map(int,input("Enter the numbers to compare, seperated by a space: ").split())
print(min(num), " is the minimum of these numbers.")


#///////////////////////////////////////////////////////////////////#
#Divide two user input numbers and round the answer following standard rounding rules. 
x, y = map(int, input("Enter the numbers to compare, seperated by a space: ").split())
print(round(x/y)," is the rounded answer.")


#///////////////////////////////////////////////////////////////////#
#Given a variable sized user-input array of digits, find the average  *excluding* the last digit and round the answer.   
import statistics

array = [int(n) for n in input("Enter the numbers to compare, seperated by a space: ").split()[:-1]]
answer = statistics.mean(array)
print(round(answer), ' ')


#///////////////////////////////////////////////////////////////////#
#Given a variable sized user-input array of digits, find the highest value. 
array = [int(n) for n in input("Enter the numbers to compare, seperated by a space: ").split()]
array.sort()
print(array[-1], " is the highest number in the given array.")


#///////////////////////////////////////////////////////////////////#
#Count the number of occurances for all digits in a variable sized user-input array of digits.
#Print occurances of 0's, 1's, 2's, 3's ...  
array = [int(x) for x in input("Enter the numbers seperated by a space:").split()]
Set = sorted(set(array))
answer = [array.count(i) for i in Set]

for i in range(len(answer)):
    print(answer[i], " ")
    

#///////////////////////////////////////////////////////////////////#
#Determine if a user-input string is a palindrom. Remove all non-alphabetical characters before testing.   
stringArr = ''.join([i for i in input("Enter the string: ").lower() if i.isalpha()])
if (stringArr == stringArr[::-1]): 
    print("The two strings are palindromes.")
else: 
    print("The two strings are not palindromes.")     

#///////////////////////////////////////////////////////////////////#
#Determine if two user input strings are permutations of each other
def isPermutation(str1, str2):
    return len(str1) == len(str2) and set(str1) == set(str2)

print(isPermutation(input("Enter first string: "), input("Enter second string: ")))


#///////////////////////////////////////////////////////////////////#
#Take a user-inputted array of numbers. Sort the array. Print each value of it's initial index.
#E.G. array[0]=4, array[1]=2 and array[2]=5 as the given array will return 1,0,2

#>> Automatically thought to use enumerate for this, and then discovered index() was a thing. Added both snippets. 
array = list(map(int, input("Enter numbers seperated by a space: ").split()))
arraySorted = array[:] #putting .sort() after the [:] returns none. Putting arraySorted = array.sort() would sort both. 
arraySorted.sort()

for num in arraySorted:
    for index, item in enumerate(array):
        if num == item: 
            print(index, " ")

#>> Above problem using index() instead. Which is way cooler.
array = list(map(int, input("Enter numbers seperated by a space: ").split()))
arraySorted = array[:]
arraySorted.sort()     

for num in arraySorted:
    print(array.index(num), " ")
    

#///////////////////////////////////////////////////////////////////#
#Given two lists, A and B, map position of all A values to the index where they appear in B. There can be duplicates, all elements in A appear in B.
list = []
for num in A:
    list.append(B.index(num))
return list

#///////////////////////////////////////////////////////////////////#
#Given a user input string, give a list of all permutations possible
def setNode(str_Pool, str_Ans, list_Ans):
    if(str_Pool):
        for i in range(len(str_Pool)):
            temp_Pool = str_Pool[:i] + str_Pool[(i+1):]
            temp_Ans = str_Ans[:] + str_Pool[i]
            setNode(temp_Pool, temp_Ans, list_Ans)
    else:
        list_Ans.append(str_Ans)

listy = []            
setNode(input("Enter string: "), '', listy)
print(list(set(listy)))
 
#///////////////////////////////////////////////////////////////////#
#Given two strings, find out if they are permutations of each other. 

def isPerm(str1, str2):
    return len(str1) == len(str2) and set(str1) == set(str2)

#///////////////////////////////////////////////////////////////////#
#Given a string, find if the string contains repeating characters

def has_Repeating(str):
    return not len(str) == len(set(str))

#///////////////////////////////////////////////////////////////////#
#Given a string, reverse the string but exclude the last elemment before reversal.

def reverse_str(str):
    return str[::-1][1:]

#[:-1:-1] doesn't work if you wanted to do one slice, but this is a workaround: 

def reverse1(str):
    buffer = len(str)-2
    return str[buffer::-1]

#///////////////////////////////////////////////////////////////////#




