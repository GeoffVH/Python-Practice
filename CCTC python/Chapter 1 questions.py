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
    for k, g in groupby(str1):
        ans += k
        rep = str(len(list(g)))
        if rep!='1':
            ans += rep
    return ans
	
