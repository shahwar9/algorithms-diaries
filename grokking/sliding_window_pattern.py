import math
from collections import defaultdict

#  s
# [2, 1, 5, 1, 3, 2] k = 3 -> ans = 9
#        e
# max sum = 8
# window_sum = 8
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
def max_sub_array_of_size_k(k, arr):
    window_start, window_sum = 0, 0
    max_sum = 0

    for window_end in range(len(arr)):
        # Keep moving window end
        window_sum += arr[window_end]

        # Check if window size is valid, or larger than k
        # In this case, calculate new max sum and prepare window_start and window_sum for next iteration.
        # This approach utilizes the window_start element and then moves the window start cursor one step ahead.
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1

    # Complexity:
    # Time: O(N) each element is traversed only once.
    # Space: O(1) no extra space required.
    return max_sum

#     s
# [2, 1, 5, 2, 3, 2], S=7
#        e
#
# min_length = -inf
# win_sum = 8
def smallest_subarray_with_given_sum(s, arr):
    window_start, window_sum = 0, 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0

    # Complexity:
    # Time: O(N+N) because each element will only be seen once in a for loop.
    # Space: O(1) no extra memory required except a few variables.
    return min_length

# Given a string, find the length of the longest substring in it with no more than K distinct characters.

#         s
# a r a a c i", K=2 => 4 "
#           e
#
# c : 1
# i : 1
def longest_substring_with_k_distinct(str1, k):
    window_start, max_len = 0, 0
    char_count = defaultdict(int)

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        char_count[right_char] += 1

        while len(char_count) > k:
            left_char = str1[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    # Complexity:
    # Time: O(N+N) because each element will only be seen once in a for loop.
    # Space: O(1) no extra memory required except a few variables.
    return max_len


# Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.
# Similar as above question except k = 2.
def fruits_into_baskets(fruits):
    window_start, max_len = 0, 0
    fruit_count = defaultdict(int)

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        fruit_count[right_fruit] += 1

        while len(fruit_count) > 2:
            left_fruit = fruits[window_start]
            fruit_count[left_fruit] -= 1
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    # Complexity:
    # Time: O(N+N) because each element will only be seen once in a for loop. Inner while can run at the most N size.
    # Space: O(1) no extra memory required except a few variables.
    return max_len

# Given a string, find the length of the longest substring, which has no repeating characters.
#       s
# a b c c d e => 3 (abc, cde)
#       e
# a: 0
# b: 1
# c: 2

def non_repeat_substring(str1):
    window_start, max_len = 0, 0
    index_map = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in index_map:
            window_start = max(window_start, index_map[right_char]+1 )

        index_map[right_char] = window_end

        max_len = max(max_len, window_end - window_start + 1)
    # Complexity:
    # Time: O(N) because each element will only be seen once in a for loop. Inner while can run at the most N size.
    # Space: O(1) no extra memory required except a few variables.
    return max_len

if __name__=="__main__":
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

