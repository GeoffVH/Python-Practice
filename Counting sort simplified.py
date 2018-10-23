#Trying to condense the typical counting sort into something more streamlined.
#Objective is to see just how simplified I can turn the original code, without making it unreadable.  

#Original counting sort Obtained from http://www.learntosolveit.com/python/algorithm_countingsort.html
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
#First itteration at condensing, which I think is the cleanest way to write this without losing O(n)
def counting_Sort1(arr):
    highest = max(arr) + 1
    count = [0] * (highest)
    ans = []

    for num in set(arr):
        count[num] = arr.count(num)
    for rep, i in zip(count, range(highest)):
        ans.extend([i] * rep)              
    return ans
    
 #//////////////////////////////////////////////////////#  
 #Second itteration at condensing, slightly more condensed but ans becomes a little more difficult to understand at a glance
 def counting_Sort2(arr):
    highest = max(arr) + 1
    count = [0] * (highest)
    
    for num in arr:
        count[num]+=1
    ans = [[i]*rep for rep, i in zip(count, range(highest)) if rep]
    return sum(ans, [])

#//////////////////////////////////////////////////////#  
#Final itteration at condensing, loses the O(n) in exchange for O(n^2) due to count being O(n) but it's easier to read than the second itt. 
def counting_Sort3(arr):
    count = [[i] * arr.count(i) for i in range(max(arr)+1)]
    return sum(count, [])
