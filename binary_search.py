# naive search scans the entire list and asks if its equal to the target. If yes, it returns the index else -1
import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] ==target:
            return [i]
    return -1

# binart search uses divide and conquer

def binary_search(l, target, low =  None, high = None): # low and high are indices
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1 # highest possible index

    if high < low:
        return -1
    # example l = [1,3,5,12,15] ; if targe is 12 (i.e searching for 10) it should return 3 index
    midpoint = (low + high) // 2 # discarding remainders : i.e. how many times to go into length and gives approximately the midpoint of the index

    if l[midpoint] == target: #if target = 12 and mispoint = 5, goes to elif
        return midpoint

    elif target < l[midpoint]: # target = 12 but midpoint is 5 so it returns binary_search (basically saying to chop off half of the list and iterate only one section of it. In this case the left half of the list is cut)
        return binary_search(l, target, low, midpoint - 1) # if true check the left half of the list (below 5)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high) # if true checks the right half of the list

if __name__=='__main__':
    l = [1,3,5,12,15,16]
    target = 15
    print(naive_search(l,target))
    print(binary_search(l,target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")
