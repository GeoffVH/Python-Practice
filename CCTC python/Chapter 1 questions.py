#////////////////////////////////////////#
#			Question 1
#Is  Unique:  Implement an algorithm  to  determine  if  a string  has  all unique characters. 
#What if you can't use additional data structures?

def is_Unique(str):
	return len(str) == len(set(str))

#No additional data structures	
def is_Unique_alt(str):
	str.sort()
	for i in range(len(str)-1):
		if str[i] != str[i+1]
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

def URL1(str):
    listy = ['20%' if char == ' ' else char for char in str]
    return ''.join(listy)
	
def URL2(str):
    return '20%'.join(listy.split())

def URL3(str):
    return str.replace(' ', '20%')
	
	
#////////////////////////////////////////#
#			Question 4
# Palindrome Permutation:  Given a string, write a function to check  if  it  is  a permutation  of
# a palindrome. A palindrome  is  a word or phrase that  is  the same forwards and backwards. A
# permutation  is  a rearrangement  of  letters. The palindrome does  not  need to  be  limited to just
# dictionary words.

def is_Permutation(str):
    odd = 0
    for char in set(str):
        if str.count(char)%2 != 0:
            odd+=1
    return odd<=1

	
