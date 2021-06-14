import math
from collections import defaultdict

# Pattern Usage:
# The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm
# that uses two pointers which move through the array (or sequence/LinkedList) at different speeds.
# This approach is quite useful when dealing with cyclic LinkedLists or arrays.
#
# By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that
# the two pointers are bound to meet. The fast pointer should catch the slow pointer once
# both the pointers are in a cyclic loop.
#
# One of the famous problems solved using this technique was Finding a cycle in a LinkedList.
# Let’s jump onto this problem to understand the Fast & Slow pattern.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    # Complexity:
    # Time: O(N)
    # Space: O(1)
    return False

# Given the head of a LinkedList with a cycle, find the length of the cycle.

def find_cycle_length(head):
    def _cycle_length(slow):
        temp = slow.next
        length = 1
        while temp != slow:
            temp = temp.next
            length += 1

        return length

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return _cycle_length(slow)
    return 0

def find_cycle_start(head):
    list_length = find_cycle_length(head)
    p1, p2 = head, head
    for i in range(list_length):
        p2 = p2.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1

def find_happy_number(num):
    hashset = set()
    square_sum = num
    while square_sum not in hashset:
        hashset.add(square_sum)
        square_sum = sum([int(digit)*int(digit) for digit in str(square_sum)])

        if square_sum == 1:
            return True

    # Time: O(logN)
    # Say N > 1000, N has M digits. Next number is N1
    # when all digits are 9, then at the most sum of squares is 9^2 M or 81M
    # N1 < 81M
    # Also, M = log(1+N)
    # N1 < 81*log(1+N) => N1 = O(logN)
    # Space: O(logN)
    return False

def find_happy_number_fsp(num):
    def _calc_square_sum(num):
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit*digit
            num //= 10
        return _sum

    fast, slow = num, num
    while True:
        slow = _calc_square_sum(slow)
        fast = _calc_square_sum(_calc_square_sum(fast))
        if fast == slow:
            break
    # Time: O(logN)
    # Say N > 1000, N has M digits. Next number is N1
    # when all digits are 9, then at the most sum of squares is 9^2 M or 81M
    # N1 < 81M
    # Also, M = log(1+N)
    # N1 < 81*log(1+N) => N1 = O(logN)

    # Space: O(1)
    return slow == 1

# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
#
# If the total number of nodes in the LinkedList is even, return the second middle node.
#           s
# 1 -> 2 -> 3 -> 4 -> 5 -> null
#                     f
#                s
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
#                               f
def find_middle_of_linked_list(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be in the original form once
# the algorithm is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of
# nodes in the LinkedList.
#
# s
# 2 -> 4 -> 6 -> 4 -> 2
#
def is_palindromic_linked_list(head):

    def _reverse_linked_list(head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

def reverse_linked_list(head):
    prev = None
    while head:
        next_temp = head.next
        head.next = prev
        prev = head
        head = next_temp

    return prev

def print_linked_list(head):
    while head:
        print(head.value)
        head=head.next

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle))

    head = reverse_linked_list(head)
    print_linked_list(head)
    print_linked_list(reverse_linked_list(head))
    # print("LinkedList has cycle: " + str(has_cycle(head)))
    # print("LinkedList cycle length: " + str(find_cycle_length(head)))
    # print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    #
    # head.next.next.next.next.next.next = head.next.next.next
    # print("LinkedList has cycle: " + str(has_cycle(head)))

def minSumOfLengths(arr, target):
    INF = len(arr) + 1
    best_at_i = [INF] * len(arr)  # the ith index represents the smallest length subarray we've found ending <= i that sums to target
    best = INF  # output
    curr_sum = 0  # current sum between left and right

    left = 0
    for right in range(len(arr)):
        # update the running sum
        curr_sum += arr[right]

        # arr is strictly positive, so shrink window until we're not above target
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left += 1

        if curr_sum == target:
            # we have a new shortest candidate to consider
            best = min(best, best_at_i[left - 1] + right - left + 1)
            best_at_i[right] = min(best_at_i[right - 1], right - left + 1)
        else:
            # best we've seen is the previous best (overlaps to end if right == 0)
            best_at_i[right] = best_at_i[right - 1]

        print(best_at_i)

    if best == INF:
        return -1
    return best

if __name__=="__main__":
    # main()
    print(minSumOfLengths([1,2,2,3,2,6,7,2,1,4,8], 5))

