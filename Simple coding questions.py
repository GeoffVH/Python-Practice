# Simple coding questions found from different online sources that I answered.
# Started with really basic question. 

#Find the minimum of an unknown amount of entries. 
num = map(int,input("Enter the numbers to compare, seperated by a space: ").split())
print(min(num), ' is the minimum of these numbers.')

#Divide two user input numbers and round the answer. 
x, y = map(int, input().split())
print(round(x/y),' is the rounded answer.')

#Take a user input string and count the number of vowels. Include y as a vowel.
#Input can include any character including uppercase characters. 
count = 0
for char in input().lower():
    if char in "aouiey": 
        count += 1
print(count, " is the amount of vowls in the given string")

#Reverse a given string.
print(input()[::-1])

#Given a string array of digits, find the average without including the last digit and round the answer.   
import statistics

array = [int(n) for n in input().split()[:-1]]
answer = statistics.mean(array)
print(round(answer), ' ')

