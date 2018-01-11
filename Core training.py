"""
Training on syntactic sugar, and alternate ways of doing core tasks.
This is all snippet code. The file isn't meant to be run as a whole.
"""

#///////////////////////////////////////////////////////////////////#
#One line variable switiching
x = 10
y = 'Ten'
print(x, y)

x, y = y, x
print(x, y)

#///////////////////////////////////////////////////////////////////#
#Creating new types in a dynamic manner

NewType = type("NewType", (object,), {"function": "I'm NewType's function."})
myNewType = NewType()
print(myNewType.function)

#Basically does exactly this:
class NewType(object):
     function = "I'm NewType's function"
myNewType = NewType()
print(myNewType.function)

#///////////////////////////////////////////////////////////////////#
#Shortcuts in if-else syntax, useful for confusing co-workers
#[on_true] if [expression] else [on_false]
#Reads exactly as english basically. It's neat.
#if you start using nested if-else using this, co-workers will inevitably murder you.
n = 10
print("This should be printed") if n == 10 else print("Ruh roh")


#///////////////////////////////////////////////////////////////////#
#Quick assignment from anything itterable to new variables, useful with map.
tinyList = ['1',2,'3']

x, y, z = tinyList    #List size must = the number of variables exactly!
print("One here: ", x)
print("Two here: ", y)
print("Three here: ", z)

x, y, z = map(int, tinyList)
print(type(x), " x should be an int class. 1 should be here: ", x)


#///////////////////////////////////////////////////////////////////#
#Constructs strings pretty easily from lists
myStringList = ["Please", "give", "this","string","spaces", ":("]
myFixedString = ' '.join(myStringList)
print(myFixedString)


#///////////////////////////////////////////////////////////////////#
#Merging two lists together side by side
myList = ['one', 'two', 'three', 'four']
myOtherList = [1, 2, 3, 4]
for x, y in zip(myList, myOtherList):
    print(x, ' ', y)

#///////////////////////////////////////////////////////////////////#
#Append one list to the end of another quickly
#Works with dicts, sets and other stuff afaik

myList = ['one', 'two', 'three', 'four']
myOtherList = [1, 2, 3, 4]

finalList = [*myList, *myOtherList]
print(finalList)

#///////////////////////////////////////////////////////////////////#
#Combining dicts together using same logic as above snippet
myDict = {'y': 5, 'x': 6}
myOtherDict = {'z': 3, 'a': 2}

combinedDict = {**myDict, **myOtherDict}
print(combinedDict)
#{'y': 5, 'x': 6, 'z': 3, 'a': 2}

#///////////////////////////////////////////////////////////////////#
#Merging a 2D list into a 1D list side by side
import itertools

mylist = [['One', 2], ['Three', 4], ['Five', 6]]
fixedList = list(itertools.chain.from_iterable(mylist))
print(fixedList)


#///////////////////////////////////////////////////////////////////#
#Using counter from collections to match anagrams
from collections import Counter

myGoodString = "listen"
myOtherGood  = "silent"
myBadString = "Not an anagram"

good = Counter(myGoodString) == Counter(myOtherGood)
bad = Counter(myBadString) == Counter(myGoodString)
print("This should be true: ", good, " This should be false: ", bad)


#///////////////////////////////////////////////////////////////////#
#Different ways to convert a string of numbers into a list of ints.

myString = "123456789"
newList = [int(char) for char in myString]
print(newList, type(newList[2]))

newList = list(map(int,myString))
print(newList, type(newList[2]))


#///////////////////////////////////////////////////////////////////#
#Using loop comprehensions with if statments
myString = "P#leas^e///# remo0ve w^eird **(chara!cters!?) +=-"
fixedList = [i for i in myString if i.isalpha() or i.isspace()]
fixedString = ''.join(fixedList)
print(fixedString)

#///////////////////////////////////////////////////////////////////#
#Other cool uses putting generators with loop comprehensions, lets you escape intermediate storage
#Can be useful to speed things up.
# x=(n for n in foo if bar(n))
# for n in x:

n = ([a,b] for a in range(0,2) for b in range(4,6))
for i in n:
    print(i)


#///////////////////////////////////////////////////////////////////#
#Get index and value side by side from anything itterable.

myList = ['A', 'B', 'C3P0', 4, 'High Five']
for index, item in enumerate(myList):
    print(index, item)

#///////////////////////////////////////////////////////////////////#
#Sending lists, sets and dictionaries to a function as a whole.

def foo(x, y):
    print(x, y)

myList = [1, 2]
mySet = (3, 4)
myDict = {'y': 5, 'x': 6}

#foo(myList)    #won't work
foo(*myList)    #prints 1, 2
foo(*mySet)     #prints 3, 4
foo(*myDict)    #prints y, x
foo(**myDict)   #prints 5, 6

#///////////////////////////////////////////////////////////////////#
#Different ways to reverse a list, string, ect.

#reverses everything, no problems.
def using_Slice(myItem):
    print(myItem[::-1])

def using_Reversed(myItem):
    print([char for char in reversed(myItem)])

def using_Reversed_alt(myItem):
    for char in reversed(myItem):
        print(char)

#Reverses a list, but not a string!
def using_Reverse(myItem):
    myItem.reverse()
    print(myItem)

myString = "Hello World!"
tinyList = [1,2,3]
using_Slice(tinyList) 
using_Reversed(tinyList)
using_Reversed_alt(myString)
using_Reverse(tinyList)
