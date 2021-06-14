def is_palindrome(arr):

    for i in range(len(arr)//2):
        if arr[i] != arr[~i]:
            return False

    return True

# Find if a number is palindrome or not.

# 69396
def is_num_palindrome(num):
    num = abs(num)

    while num >= 10:
        digits = int(math.log(num, 10))
        first = num // (10**digits)
        last = num % 10
        print(first, last)
        if first != last:
            return False
        num = num % (first*(10**digits))
        num //= 10

        print(num)
    return True

def binary_search(arr, key):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            left = mid+1
        else:
            right = mid-1

    return -1

def find_low_high(arr, key):
    low = binary_search(arr, key)
    print(low)
    print(arr[low-1])
    while arr[low] == key:
        low -= 1
    print(low)
    high = binary_search(arr, key)

    while arr[high] == key:
        high += 1
    return [low+1, high-1]

def remove_duplicate_words(sent):
    words = sent.split()
    i = 1

    while i < len(words):
        if words[i].strip("!") == words[i-1].strip("!"):
            words[i-1] = ""

        i+=1
    print(" ".join(words).strip())


def forward_backward_pairs(sent):
    words = sent.split()
    i = 0
    while i < len(words)//2:
        print(" ".join([words[i], words[~i]]))
        i+=1

    if len(words)%2:
        print(words[i])

def sorted_words_in_matrix(sent):
    # sort words.
    words = sent.split()
    words.sort()

    C = 3
    R = math.ceil(len(words)/C)

    max_len = max([len(w) for w in words])

    # number of empty spaces margin.
    empty_margin = C*R - len(words)

    M = []
    for r in range(R):
        M.append([" "*max_len]*C)

    i = 0
    for c in range(C):
        for r in range(R):
            # Decide if you need to add space or a word to matrix based on empty place margin left.
            if empty_margin > 0 and r == R-1:
                M[r][c] = " "
                empty_margin -= 1
                continue
            else:
                if i < len(words):
                    M[r][c] = words[i]
                else:
                    M[r][c] = " "
                    empty_margin -= 1
            i+=1

    # Calculate max_length of string in each column.
    # This is used for alligning different strings in matrix.
    max_lens = [max([ len(M[r][c])  for c in range(C) for r in range(R) if c==0])]
    max_lens.append(max([ len(M[r][c])  for c in range(C) for r in range(R) if c==1]))
    max_lens.append(max([len(M[r][c]) for c in range(C) for r in range(R) if c == 2]))

    # Apply Space adjustment.
    for c in range(C):
        for r in range(R):
            M[r][c] = M[r][c].rjust(max_lens[c])

    # Print the final matrix in final form.
    for r in M:
        str = "| " + " ".join(r)+ " |"
        print(str)

#   next_temp ->
# ...<-2  3 -> 4 -> ...
#      <-prev
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next= next



if __name__=="__main__":
    # forward_backward_pairs("There a message in text this hidden secret is")
    remove_duplicate_words("Code Code! Nice Code")
    # A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # # print(binary_search(A, 6))
    # B = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
    # print(find_low_high(B, 2))