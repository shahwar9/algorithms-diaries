import math
from collections import defaultdict

# Pattern Usage:
# In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that
# fulfill certain constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair,
# a triplet or even a subarray.
#


# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
#
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
#             l
# 1, 2, 3, 4, 6 target=20
#             r
# [-1, -1]
def pair_with_targetsum(arr, target_sum):
    lp, rp = 0, len(arr)-1

    while lp < rp:
        current_sum = arr[lp]+arr[rp]
        if current_sum == target_sum:
            return [lp, rp]

        if current_sum > target_sum:
            rp -= 1
        else:
            lp += 1

    # Complexity:
    # Time: O(N) because on the worst each element will be seen once. As soon as lp == rp the loop terminates.
    # Space: O(1) as no extra element is created depending on N.

    return [-1, -1]

def pair_with_targetsum_hash(arr, target_sum):
    comp_map = {}

    for i in range(len(arr)):
        print(comp_map)
        if target_sum - arr[i] in comp_map:
            return [i, comp_map[target_sum - arr[i]]]
        else:
            comp_map[arr[i]] = i

    # Complexity:
    # Time: O(N)
    # Space: Because we end up adding at the most N elements.
    return [-1, -1]

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing
# the duplicates in-place return the length of the subarray that has no duplicate in it.
#                    d
# [2, 3, 4, 5, 6, 7, 9] => 4
#                    n
# next_non_duplicate: Next position to put non duplicate number.
# next: points next element to match next_non_duplicate-1 number with.
def remove_duplicates(arr):
    next_non_duplicate, next = 1, 1

    while next < len(arr):
        last_unique = next_non_duplicate - 1
        if arr[last_unique] != arr[next]:
            arr[next_non_duplicate] = arr[next]
            next_non_duplicate += 1

        next += 1

    # Complexity:
    # Time: O(N)
    # Space: Because we end up adding at the most N elements.
    return next_non_duplicate

# Given an unsorted array of numbers and a target ‘key’, remove all instances
# of ‘key’ in-place and return the new length of the array.
#  r
# [3, 2, 3, 6, 3, 10, 9, 3], Key=3
#  i
def remove_key(arr, key):
    replace_point = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[replace_point] = arr[i]
            replace_point += 1

    # Complexity:
    # Time: O(N)
    # Space: Because we end up adding at the most N elements.
    return replace_point

# Given a sorted array, create a new array containing squares of all
# the numbers of the input array in the sorted order.
#                p2
# [-2, -1, 0, 2, 3]
#  p1
def make_squares(arr):
  squares = [0 for _ in range(len(arr))]
  rp, lp = len(arr)-1, 0
  squares_pointer = len(squares)-1

  while squares_pointer >= 0:
      rs = arr[rp] * arr[rp]
      ls = arr[lp] * arr[lp]

      if rs > ls:
          squares[squares_pointer] = rs
          rp -= 1
      else:
          squares[squares_pointer] = ls
          lp += 1

      squares_pointer -= 1

  # Complexity:
  # Time: O(N)
  # Space: O(N)
  return squares

# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Sorted:[-3, -2, -1, 0, 1, 1, 2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
def search_triplets(arr):
    def _search_pair(arr, target_sum, left, triplets):
        right = len(arr) -1

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1

            if current_sum > target_sum:
                right -= 1
            else:
                left += 1

    arr.sort()
    triplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        _search_pair(arr, -arr[i], i+1, triplets)

    # Complexity:
    # Time: O(NlogN + N^2) ( sort + _search_pair is O(N) and called N times.)
    # Space: O(N) Because of the sort.
    return triplets

# Given an array of unsorted numbers and a target number, find a triplet in the array whose
# sum is as close to the target number as possible, return the sum of the triplet.
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# [-2, 0, 1, 2], target=2
#
#

# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers
# of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
#        l
# [0, 0, 1, 1, 2]
#           h
#           i
#
#  l
# [0, 1 1, 2, 2, 2]
#       h
#       i
def dutch_flag_sort(arr):
    low, high = 0, len(arr)-1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[low], arr[i] = arr[i], arr[low]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1

    # Complexity:
    # Time: O(N)
    # Space: O(1)
    return arr

if __name__=="__main__":

    # A = [1, 2, 3, 4, 6]
    # target=6
    # print("Hash: "+ str(pair_with_targetsum_hash(A, target)))
    # print("2 Pointer: "+ str(pair_with_targetsum(A, target)))
    #
    # print("Remove Key: " + str(remove_key([3, 2, 3, 6, 3, 10, 9, 3], key=3)))
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Search triplets"+str(search_triplets([-3, 0, 1, 2, -1, 1, -2])))
