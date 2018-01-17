# Simple coding questions found from different online sources that I answered for practice.
# Started with basic questions to test out python I've learned.  


#Find the minimum of a variable amount of entries. 
num = map(int,input("Enter the numbers to compare, seperated by a space: ").split())
print(min(num), " is the minimum of these numbers.")


#Divide two user input numbers and round the answer. 
x, y = map(int, input("Enter the numbers to compare, seperated by a space: ").split())
print(round(x/y),' is the rounded answer.')


#Take a user input string and count the number of vowels. Include y as a vowel.
#Input can include any character including uppercase characters. 
#I considered using counter, but it's not shorter or more readable. Simple is king. 
count = 0
for char in input("Enter the string: ").lower():
    if char in "aouiey": 
        count += 1
print(count, " is the amount of vowls in the given string")


#Reverse a given string.
print(input("Enter the string: ")[::-1])


#Given a variable sized user-input array of digits, find the average without including the last digit and round the answer.   
import statistics

array = [int(n) for n in input("Enter the numbers to compare, seperated by a space: ").split()[:-1]]
answer = statistics.mean(array)
print(round(answer), ' ')


#iven a variable sized user-input array of digits, find the highest value. 
array = [int(n) for n in input("Enter the numbers to compare, seperated by a space: ").split()]
array.sort()
print(array[-1], " is the highest number in the given array.")


#Count the number of occurances for all digits in a variable sized user-input array of digits.
#Print occurances of 0's, 1's, 2's, 3's ...  
array = [int(x) for x in input("Enter the numbers seperated by a space:").split()]
Set = sorted(set(array))
answer = [array.count(i) for i in Set]

for i in range(len(answer)):
    print(answer[i], " ")
    

#Determine if a user-input string is a palindrom. Remove all non-alphabetical characters before testing.   
stringArr = ''.join([i for i in input("Enter the string: ").lower() if i.isalpha()])
if (stringArr == stringArr[::-1]): 
    print("The two strings are palindromes.")
else: 
    print("The two strings are not palindromes.")     


#Take a user-inputted array of numbers. Sort the array. Print each value of it's initial index.
#E.G. array[0]=4, array[1]=2 and array[2]=5 as the given array will return 1,0,2

#Automatically thought to use enumerate for this, and then discovered index() was a thing. Added both snippets. 
array = list(map(int, input("Enter numbers seperated by a space: ").split()))
arraySorted = array[:] #putting .sort() after the [:] returns none. Putting arraySorted = array.sort() would sort both. 
arraySorted.sort()

for num in arraySorted:
    for index, item in enumerate(array):
        if num == item: 
            print(index, " ")

#Above problem using index() instead.
array = list(map(int, input("Enter numbers seperated by a space: ").split()))
arraySorted = array[:]
arraySorted.sort()     

for num in arraySorted:
    print(array.index(num), " ")
 
