import random
import time
# search through every index in the list
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search 
# divide the list and search in the correct half 
def binary_search(l, target, low = None, high = None):
    # for the initial run
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low: # The number isn't in the list: The high keeps decreasing or the low keeps increasing until low > high
        return -1
    # the middle index in the list
    mid_point = (low + high) // 2
    # binary research
    if target == l[mid_point]:
        return mid_point
    elif target < mid_point: #search in the left half of the list
        return binary_search(l, target, low, mid_point - 1)
    else: # target > mid_point
        return binary_search(l, target, mid_point + 1, high) #search in the right half of the list
    

# l = [1, 3, 5, 10, 12]
# target = 10
# print(naive_search(l, target))
# print(binary_search(l, target))


#Making a random list of 1000 number
length = 1000
sorted_list = set() #Making a set first to only add unique numbers

# A loop to add random numbers
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))

# Convert the set to a sorted list
sorted_list = sorted(list(sorted_list))

# timing naive search
start = time.time()
for target in sorted_list: # iterating through ever element
    naive_search(sorted_list, target)
end = time.time()
print(f'Naive search time: {(end - start)/length} seconds') # the time per iteration

# timing binary search
start = time.time()
for target in sorted_list: # iterating through ever element
    binary_search(sorted_list, target)
end = time.time()
print(f'Binary search time: {(end - start)/length} seconds') # the time per iteration



