#////////////////////////////////////////#
#			Question 1
#Is  Unique:  Implement an algorithm  to  determine  if  a string  has  all unique characters. 
#What if you can't use additional data structures?

def is_Unique(str1):
	return len(str1) == len(set(str1))

#No additional data structures	
def is_Unique_alt(str1):
	str1.sort()
	for i in range(len(str1)-1):
		if str1[i] != str1[i+1]
			return false
	return true


#////////////////////////////////////////#
#			Question 2
#Given two strings, write a method to decide  if  one  is  a permutation of  the other.

def isPerm(str1, str2):
	return len(str1) == len(str2) and set(str1) == set(str2)
	

#////////////////////////////////////////#
# 			Question 3
# Write a  method  to replace  all  spaces  in  a string with '%20: 
# You  may assume  that  the  string has sufficient space at  the  end  to hold  the  additional characters,  and  that  you are given  the  "true"
# length of  the  string.

def URL1(str1):
    listy = ['20%' if char == ' ' else char for char in str1]
    return ''.join(listy)
	
def URL2(str1):
    return '20%'.join(str1.split())

def URL3(str1):
    return str1.replace(' ', '20%')
	
	
#////////////////////////////////////////#
#			Question 4
# Palindrome Permutation:  Given a string, write a function to check  if  it  is  a permutation  of
# a palindrome. A palindrome  is  a word or phrase that  is  the same forwards and backwards. A
# permutation  is  a rearrangement  of  letters. The palindrome does  not  need to  be  limited to just
# dictionary words.

def is_Permutation(str1):
    odd = 0
    for char in set(str):
        if str.count(char)%2 != 0:
            odd+=1
    return odd<=1

#////////////////////////////////////////#
#			Question 6
# String Compression:  Implement a method to perform basic string compression using  the  counts
# of repeated characters.  For  example,  the  string  aabcccccaaa  would become  a2blc5a3 .  If  the
# "compressed" string would not become smaller than  the  original string, your method should return
# the  original string.  You  can assume the string has only uppercase and lowercase letters  (a  - z).

from itertools import groupby

def compress(str1):
    ans = ''
    for key, group in groupby(str1):
        ans += key
        rep = str(len(list(group)))
        if rep!='1':
            ans += rep
    return ans

#////////////////////////////////////////#
#			Question 8
# String Rotation:  Assume you have a method  i5Substring  which checks if one word  is  a substring
# of another.  Given  two strings, S1 and S2, write code to check  if  S2  is  a rotation of S1 using only one
# call  to  isSubstring  (e.g.,  U waterbottle uis  a rotation ofu erbottlewat U ).

#Is there a way to find out where the split is done? -> We can use find if so.
#Alternative? Set and len must match of course, but that won't catch all possible exceptions. 
#s2 in s1 would catch all cases but also extra.
#can I return where s2 was found in s1? 

#////////////////////////////////////////#
#			Question 8
# String Rotation:  Assume you have a method  i5Substring  which checks if one word  is  a substring
# of another.  Given  two strings, S1 and S2, write code to check  if  S2  is  a rotation of S1 using only one
# call  to  isSubstring  (e.g.,  "waterbottle" is  a rotation of "erbottlewat" ).

def isSubstring(s1, s2):
    return s1 in s2*2 and len(s1) == len(s2)

# Waterbottle = s1 and erbottleWat = s2
# s2*2 = erbottleWaterbottleWat, which contains Waterbottle so our in operator can function correctly. 
# Len() checking makes sure edge cases like s1 being "Wat" won't return a false positive. 

