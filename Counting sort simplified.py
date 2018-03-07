#Trying to condense the typical counting sort into something more streamlined. 
#Objective is to see just how pythonic you can turn the original code. 

#Original code, looks very much like something from java or C++
#Obtained from http://www.learntosolveit.com/python/algorithm_countingsort.html

def counting_sort(array, maxval):
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array
    
#//////////////////////////////////////////////////////#    
#First itteration at condensing
def counting_Sort1(arr):
    highest = max(arr) + 1
    count = [0] * (highest)
    ans = []

    for num in arr:
        count[num] += 1
    for rep, i in zip(count, range(highest)):
        ans.extend([i] * rep)              
    return ans
    
 #//////////////////////////////////////////////////////#  
 #Second itteration at condensing
 def counting_Sort2(arr):
    highest = max(arr) + 1
    count = [0] * (highest)
    
    for num in arr:
        count[num]+=1
    ans = [[i]*rep for rep, i in zip(count, range(highest)) if [i]*rep ]
    return sum(ans, [])

#//////////////////////////////////////////////////////#  
#Final itteration at condensing
def counting_Sort3(arr):
    count = [[i] * arr.count(i) for i in range(max(arr)+1) if arr.count(i)]
    return sum(count, [])
