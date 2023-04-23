import random
import time


# Implementation of binary search
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Proving that binary search is faster than naive search or linear search on average
# If the value is present, return the index
# if not, return -1

def naive_search(list, target):
    for i in range(len(list)):  #  condition uses length of list so each value of i the reference for the list index
        if list[i] == target:  # the list parameter uses the i as reference if the value is equal to target
            return list[i]
        
    return -1




# Binary search leverages the fact that the list is SORTED

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
        
    #  If the target is not in this list
    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    
    if list[midpoint] == target:
        return list[midpoint]
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        #  Target > list[midpoint]
        return binary_search(list, target, midpoint+1, high)
    

if __name__=='__main__':
    l = l
    target = 9
    print(naive_search(l, target))
    print(binary_search(l, target))




#  Runtime test


length = 10000
# Build sa sorted list of length 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

# Naive_search
start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print("naive_search time: ", (end - start)/length, " seconds ")


# Binary_search
start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print("Binary_search time: ", (end - start)/length, " seconds ")