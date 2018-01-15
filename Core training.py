"""
Training on syntactic sugar, and alternate ways of doing core tasks.
This is all snippet code. The file isn't meant to be run as a whole.
"""

#///////////////////////////////////////////////////////////////////#
#One line variable switiching
x = 10
y = 'Ten'
print(x, y)
#>>> 10 Ten

x, y = y, x
print(x, y)
#>>> Ten 10


#///////////////////////////////////////////////////////////////////#
#Creating new types in a dynamic manner

NewType = type("NewType", (object,), {"function": "I'm NewType's function."})
myNewType = NewType()
print(myNewType.function)
#>>> I'm NewType's function.


#Basically exactly this:
class NewType(object):
     function = "I'm NewType's function"
myNewType = NewType()
print(myNewType.function)
#>>> I'm NewType's function

#///////////////////////////////////////////////////////////////////#
#Shortcuts in if-else syntax, useful for confusing co-workers
#[on_true] if [expression] else [on_false]
#Reads exactly as english basically. It's neat.
#if you start using nested if-else using this, co-workers will inevitably murder you.
n = 10
print("This should be printed") if n == 10 else print("Ruh roh")
#>>> This should be printed

#///////////////////////////////////////////////////////////////////#
#Quick assignment from anything itterable to new variables, useful with map.

tinyList = ['1',2,'3']
x, y, z = tinyList    #List size must = the number of variables exactly!
print("One here: ",  x)     #>>> One here:  1
print("Two here: ", y)      #>>> Two here:  2
print("Three here: ", z)    #>>> Three here:  3

x, *y, z, q = [1,2,3,4,5,6,7]      #But you can cheat the above rule doing this.
print("One here: ", x)
#>>> One here:  1
print("All numbers up till the last two: ", y)
#>>> All numbers up till the last two:  [2, 3, 4, 5]
print("Six here: ", z)
#>>> Six here:  6
print("Seven here: ", q)
#>>> Seven here:  7

#Other things that work
x, y, z = (i+1 for i in range(3))
x, (y, z), q = [1, (2, 3), 4]
x, y, z = map(int, tinyList) #maps tinylist into x, y, z as ints


#///////////////////////////////////////////////////////////////////#
#Things you can do with negatives in the index spot

myList = [1,2,3,4,5,6,7,8,9,10]
print("Get the last element: ", myList[-1])
print("Get the second to last element: ", myList[-2])
print("Get the last element as a list of it's own: ", myList[-1:])
print(type(myList[-1:]))
#>>> Get the last element:  10
#>>> Get the second to last element:  9
#>>> Get the last element as a list of it's own:  [10]
#>>> <class 'list'>


#///////////////////////////////////////////////////////////////////#
#More things you can do with slicing
#General rule: [ <Start> : <End> : <Step Size> ]
#If you don't fill out a <> it falls to it's default:
#<Start = 0>, <End = Ending Index>, <Step Size = 1>

myList = [1,2,"H","e","y",3,4,5]
print("Get Hey ", myList[2:5])
print("Get Hey ", myList[-6:-3])
#>>> print("Reverse list: ", myList)
#>>> Get Hey  ['H', 'e', 'y']
#>>> Get Hey  ['H', 'e', 'y']
#>>> Reverse list:  [1, 2, 'H', 'e', 'y', 3, 4, 5]
"""
Index -> Value
    0 1
    1 2
    2 H
    3 e
    4 y
    5 3
    6 4
    7 5
"""


#///////////////////////////////////////////////////////////////////#
#You can also replace/add/remove elements with slicing.

myList = [1, 2, 3, 4, 5]
myList[2:3] = ["Hi","!"]   #Note: We're not replacing just 3. We added ! between 3 and 4.
print(myList)
#>>> [1, 2, 'Hi', '!', 4, 5]

myList[2:3] = []
print(myList)
#>>> [1, 2, '!', 4, 5]


#///////////////////////////////////////////////////////////////////#
# Getting a function to return multiple variables
def function():
	return 1, 2, 3

x, y, z = function()
print(x, y, z )     #Variables saved as ints
print(function())   #Function() returns as a tuple.
#>>> 1 2 3
#>>> (1, 2, 3)


#///////////////////////////////////////////////////////////////////#
#Merging two lists together side by side
myList = ['one', 'two', 'three', 'four']
myOtherList = [1, 2, 3, 4]
for x, y in zip(myList, myOtherList):
    print(x, ' ', y)

#>>> one   1
#>>> two   2
#>>> three   3
#>>> four   4


#///////////////////////////////////////////////////////////////////#
#Sliding window with islice

from itertools import islice

def windowSlide(arr, step):
    ans = (islice(arr, i, None) for i in range(step))
    return list(zip(*ans))

myList = [1, 2, 3, 4, 5, 6]
print(windowSlide(myList, 3))
#>>> [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
print(windowSlide(myList, 2))
#>>> [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]


#///////////////////////////////////////////////////////////////////#
#Append one list to the end of another quickly
#Works with dicts, sets and other stuff afaik

myList = ['one', 'two', 'three', 'four']
myOtherList = [1, 2, 3, 4]

finalList = [*myList, *myOtherList]
print(finalList)
#>>> ['one', 'two', 'three', 'four', 1, 2, 3, 4]


#///////////////////////////////////////////////////////////////////#
#Combining dicts together using same logic as above snippet
myDict = {'y': 5, 'x': 6}
myOtherDict = {'z': 3, 'a': 2}

combinedDict = {**myDict, **myOtherDict}
print(combinedDict)
#>>> {'y': 5, 'x': 6, 'z': 3, 'a': 2}


#///////////////////////////////////////////////////////////////////#
#You can generating Dicts on the go
myList = {x: x ** 2 for x in range(5)}
print(myList)
#>>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

myList = {x: 'a' + str(x) for x in range(10)}
print(myList)
#>>> {0: 'a0', 1: 'a1', 2: 'a2', 3: 'a3', 4: 'a4', 5: 'a5', 6: 'a6', 7: 'a7', 8: 'a8', 9: 'a9'}


#///////////////////////////////////////////////////////////////////#
#Merging a 2D list into a 1D list side by side
import itertools

mylist = [['One', 2], ['Three', 4], ['Five', 6]]
fixedList = list(itertools.chain.from_iterable(mylist))
print(fixedList)
#>>> ['One', 2, 'Three', 4, 'Five', 6]



#///////////////////////////////////////////////////////////////////#
#Multiple if statements

m = 3
if m==1 or m==3 or m==5 or m==7: print("Hello")
if m in [1,3,5,7]: print("This is the same as the above line")
#>>> Hello
#>>> This is the same as the above line


#///////////////////////////////////////////////////////////////////#
#Using Join, and using += with strings
myStringList = ["Please", "give", "this","string","spaces", ":("]
myFixedString = ' '.join(myStringList)
print(myFixedString)
#>>> Please give this string spaces :(

myFixedString = ''
for i in range(len(myStringList)):
    myFixedString += myStringList[i] + " "
print(myFixedString)
#>>> Please give this string spaces :(


#///////////////////////////////////////////////////////////////////#
#Different ways to convert a string of numbers into a list of ints.

myString = "123456789"

newList = [int(char) for char in myString]
print(newList, type(newList[2]))
#>>> [1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'int'>

newList = list(map(int,myString))
print(newList, type(newList[2]))
#>>> [1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'int'>


#///////////////////////////////////////////////////////////////////#
#Using loop comprehensions with if statments
myString = "P#leas^e///# remo0ve w^eird **(chara!cters!?) +=-"
fixedList = [i for i in myString if i.isalpha() or i.isspace()]
fixedString = ''.join(fixedList)
print(fixedString)
#>>> Please remove weird characters


#///////////////////////////////////////////////////////////////////#
#Other cool uses putting generators with loop comprehensions, lets you escape intermediate storage
#Can be useful to speed things up.
# x=(n for n in foo if bar(n))
# for n in x:

n = ([a,b] for a in range(0,2) for b in range(4,6))
for i in n:
    print(i)
#>>> [0, 4]
#>>> [0, 5]
#>>> [1, 4]
#>>> [1, 5]


#///////////////////////////////////////////////////////////////////#
#Putting lambda's into dicts is actually possible.
magicDict = {
	'sum': lambda x, y: x + y,
	'subtract': lambda x, y: x - y,
    'p': lambda x, y: print(x, y)
}

print(magicDict['sum'](12,8))
print(magicDict['subtract'](12,2))
magicDict['p']("hello", " world!")
#>>> 20
#>>> 10
#>>> hello  world!


#///////////////////////////////////////////////////////////////////#
#Get index and value side by side from anything itterable.

myList = ['A', 'B', 'C3P0', 4, 'High Five']
for index, item in enumerate(myList):
    print(index, item)
#>>> 1 B
#>>> 2 C3P0
#>>> 3 4
#>>> 4 High Five


#///////////////////////////////////////////////////////////////////#
#Setting up enum definitions

class numbers:
	A, B, C, D, E = ['A', 'B', 'C3P0', 4, 'High Five']

print(numbers.A)    #>>> A
print(numbers.B)    #>>> B
print(numbers.C)    #>>> C3P0
print(numbers.D)    #>>> 4
print(numbers.E)    #>>> High Five


#///////////////////////////////////////////////////////////////////#
#Sending lists, sets and dictionaries to a function as a whole.

def foo(x, y):
    print(x, y)

myList = [1, 2]
mySet = (3, 4)
myDict = {'y': 5, 'x': 6}

#foo(myList)     #won't work
foo(*myList)    #>>> 1, 2
foo(*mySet)     #>>> 3, 4
foo(*myDict)    #>>> y, x
foo(**myDict)   #>>> 5, 6


#///////////////////////////////////////////////////////////////////#
#Print out the most repeating number, using count shenanigans with max

myList = [1,2,3,4,2,2,2,1,4,4,4,7,3,2,8,6,4,1,2,9]
mySet = set(myList)
print(max(mySet, key = myList.count))
#>>> 2


#///////////////////////////////////////////////////////////////////#
#Print out the most repeating number, using counter shenanigans
import collections

myList = [1,2,3,4,2,2,2,1,4,4,4,7,3,2,8,6,4,1,2,9]
myCounter = collections.Counter(myList)
print( myCounter.most_common(1) )
#>>> [(2, 6)]  this means 2 is the most common, appearing 6 times.
print( myCounter.most_common(3) ) #Print out the first three most common w/ num of occurances.
#>>> [(2, 6), (4, 5), (1, 3)]


#///////////////////////////////////////////////////////////////////#
#How to use counter in for loops, or dictionaries with for loops in general. 
import collections

myString = "Hello World!"
myCounter = collections.Counter(myString)
for char, occurances in myCounter.items():
    if char in "aeiouy": 
        print(char, " occured ", occurances, " times.")
#>>> e  occured  1  times. o  occured  2  times.


#///////////////////////////////////////////////////////////////////#
#Using counter from collections to match anagrams
from collections import Counter

myGoodString = "listen"
myOtherGood  = "silent"
myBadString = "Not an anagram"

good = Counter(myGoodString) == Counter(myOtherGood)
bad = Counter(myBadString) == Counter(myGoodString)
print("This should be true: ", good, " This should be false: ", bad)
#>>> This should be true:  True  This should be false:  False


#///////////////////////////////////////////////////////////////////#
#Different ways to reverse a list, string, ect.

|def using_Slice(myItem):
    print(myItem[::-1])     #Best one to use, handles everything

def using_Reversed(myItem):
    print([char for char in reversed(myItem)])

def using_Reversed_alt(myItem):
    for char in reversed(myItem):
        print(char)

def using_Reverse(myItem):
    myItem.reverse()        #Reverses a list, but not a string!
    print(myItem)

myString = "Hello World!"
tinyList = [1,2,3]
using_Slice(tinyList)       #>>> [3, 2, 1]
using_Reversed(tinyList)    #>>> [3, 2, 1]
using_Reversed_alt(myString) #Prints !dlow olleH char by char on each line
using_Reverse(tinyList)     #>>> [3, 2, 1]
#>>> [3, 2, 1]
