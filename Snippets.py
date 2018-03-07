"""
Training on syntactic sugar, and alternate ways of doing core tasks.
This is all snippet code. The file isn't meant to be run as a whole.
"""

#///////////////////////////////////////////////////////////////////#
#Quick assignment from anything itterable to new variables.

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

x, *y = [1,2,3,4,5,6,7]
print("All numbers following 1 here: ", y)
#>>> All numbers following 1 here:  [2, 3, 4, 5, 6, 7]

#One line variable switiching using quick assignment
x = 10
y = 'Ten'
x, y = y, x
print(x, y)
#>>> Ten 10

#Works with tuples too:
(a, (b, c), d) = [(1, 2), (3, 4), (5, 6)]
print(a)
#>>> (1, 2)
print(b)
#>>> 3
print(c, d)
#>>> 4 (5, 6)

#Functions like map or generics work with quick assignment, so long as you're absolutely sure the # of variables the function returns
x, y, z = (i+1 for i in range(3))	
x, y, z = map(int, tinyList)
x, y, z = [int(i) for i in input("Type 3 numbers: ").split()]

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
#Dir is a gem that should be used more often when you want to know exactly what an object you've got can do. 

print(dir("Strings!"))
#>>> Everything built-in to strings. It's a long list. 

#///////////////////////////////////////////////////////////////////#
#Shortcuts in if-else syntax, useful for confusing co-workers
#[on_true] if [expression] else [on_false]
#Reads exactly as english basically. It's neat.
#if you start using nested if-else using this, co-workers will inevitably murder you.
n = 10
print("This should be printed") if n == 10 else print("Ruh roh")
#>>> This should be printed


#///////////////////////////////////////////////////////////////////#
#Nested loop comprehension + if/else mega guide. They're handy, just need to pay attention to setting up syntax correctly.

listy = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in listy for num in elem]
#>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

Re-wording snippet step by step
1) for elem in listy:
    for num in elem:
        add num to the list
2) for elem in listy: for num in elem: add num to the list
3) [num for elem in listy for num in elem]

#You can also set up tuples in nested loops
[(x,y) for x in range(2) for y in range(2)]
#>>> [(0, 0), (0, 1), (1, 0), (1, 1)]

you can think of it like this: 
(x,y)
 for x in range(2):
 	for y in range(2):
		add (x,y) to the list

#You can add if statements to nested loops, but be sure to get the syntax right. Here we remove the string that doesn't match the 2 num pattern.
testList = ['121212', '343434', '12341234', '565656' ]
listSets = [set('12'), set("34"), set("56")]
[str for str in testList for row in listSets if set(str.lower()) <= row]
#>>> ['121212', '343434', '565656']

str 
 for str in testList: 
 	for row in listSets: 
 		if set(str.lower()) <= row:
			add str into the list

 
#AFAIK, you can't do normal if/else at the start except using this syntax. The if/else alternate syntax,
[x if a else y for a in sequence] 

listy = [1,2,3,4,5,6,7,8,10]
["Even" if num%2==0 else 'Odd' for num in listy] 
#>>> ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Even']


#You can put if else like normal anywhere else in the loop comp however
[(x, y) for x in range(4) if x % 2 == 1 for y in range(4)]
#>>> [(1, 0), (1, 1), (1, 2), (1, 3), (3, 0), (3, 1), (3, 2), (3, 3)]

(x, y) 
 for x in range(4):
 	if x % 2 == 1:
 		for y in range(4):
			add (x,y) to the list

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
#List Gotcha. Difference between a regular list and a list composed of a list. 

myArray = [1] * 5	#Each int in the list is stored by reference. 
myArray[0] = 20		
print(myArray)
#>>> [20, 1, 1, 1, 1]
	
myArray = [[1]] * 5  #Set up list as [[1], [1], [1], [1], [1]] however lists by default store references. 
#That's why you can have ints and strings in the same list.
#So what you're doing is setting up a reference to [1] and copying that reference five times, populating the rest of the array with the same reference.
myArray[0][0] = 20   #Since you changed the value following one address, all other lookups lead back to your modification since they're all copies of the orignal. 
print(myArray)
#>>> [[20], [20], [20], [20], [20]]


#///////////////////////////////////////////////////////////////////#
#Other neat things with the * operator.

#This works the exact same with lists and sets. 
myString = "xyz" * 3
print(myString)
#>>> xyzxyzxyz


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
#Sliding window with islice. I did not come up with this one, but found it online. 

from itertools import islice

def windowSlide(arr, step):
    ans = (islice(arr, i, None) for i in range(step))
    return list(zip(*ans))

myList = [1, 2, 3, 4, 5, 6]
print(windowSlide(myList, 3))
#>>> [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
print(windowSlide(myList, 2))
#>>> [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]


#/////////////////////////////////////////////////////////////////#
#Key point of the above snippet
#Basically, zip(*a) unzips a. So if b = zip(a), then a = zip(*b)
#Ergo: turns a list of pairs in to a pair of lists

myList = [(1,2), (3,4), (5,6)]
zip(*myList)
print(zip(*myList))
#>>> [(1, 3, 5), (2, 4, 6)]


#///////////////////////////////////////////////////////////////////#
#Append one list to the end of another quickly
#Works with dicts, sets and other stuff afaik

myList = ['one', 'two', 'three', 'four']
myOtherList = [1, 2, 3, 4]

[*myList, *myOtherList]
#>>> ['one', 'two', 'three', 'four', 1, 2, 3, 4]

myList+myOtherList
#>>> ['one', 'two', 'three', 'four', 1, 2, 3, 4]

#///////////////////////////////////////////////////////////////////#
#Combining dicts together using same logic as above snippet
myDict = {'y': 5, 'x': 6}
myOtherDict = {'z': 3, 'a': 2}

combinedDict = {**myDict, **myOtherDict}
print(combinedDict)
#>>> {'y': 5, 'x': 6, 'z': 3, 'a': 2}

#///////////////////////////////////////////////////////////////////#
#Flatten a nested list
myList = [['one', 'two', 'three', 'four'],[1,2,3,4]]
sum(myList, [])
#>>> ['one', 'two', 'three', 'four', 1, 2, 3, 4]

#///////////////////////////////////////////////////////////////////#
#Quick set operations
mySet = set([1,2,3,4])
myOtherSet = set([3,4,5,6])

mySet | myOtherSet # Union
#>>> {1, 2, 3, 4, 5, 6}
mySet & myOtherSet # Intersection
#>>> {3, 4}
mySet < myOtherSet # Subset
#>>> False
mySet - myOtherSet # Difference
#>>> {1, 2}
mySet ^ myOtherSet # Symmetric Difference
#>>> {1, 2, 5, 6}


#///////////////////////////////////////////////////////////////////#
#Using sets to handle duplicates

myList = [1,2,1,1,2,3,4] 
print(set(myList))
#>>> {1, 2, 3, 4}

numInList = len(set(myList))
print("Amount of unique numbers in myList: ", numInList) 




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
def using_Slice(myItem):
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


#///////////////////////////////////////////////////////////////////#
#Setting up dicts using loop comprehensions.  
myList = [[1,'A'],['KEY','B',7,7,7],[3,'C','HELLO WORLD!']]
myDict = { e[0]:e for e in myList}
print(myDict)
#>>> {'KEY': ['KEY', 'B', 7, 7, 7], 1: [1, 'A'], 3: [3, 'C', 'HELLO WORLD!']}
        
