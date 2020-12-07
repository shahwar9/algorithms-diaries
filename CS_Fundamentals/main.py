from pprint import pprint

def knapsack_recursive(wt, val, W):
    # Smallest possible input
    if len(wt) == 0 or W == 0:
        return 0

    # Get rid of last item because weight of item is greater
    # than the W itself.
    if wt[-1] > W:
        # Advance in recursion without last item.
        return knapsack_recursive(wt[:-1], val[:-1], W)
    else:
        # Weight of last item is within W, thus, 2 possibilities are there:
        # max(consider item, not consider item)
        return max(val[-1] + knapsack_recursive(wt[:-1], val[:-1], W - wt[-1]),
                   knapsack_recursive(wt[:-1], val[:-1], W))


def knapsack_memioze(wt, val, W):
    t = []

    n = len(wt)

    # Memoization table.
    for i in range(n + 1):
        t.append([-1] * (W + 1))

    def helper_memoize(wt, val, W, n):

        # Smallest possible input
        if n == 0 or W == 0:
            return 0

        if t[n][W] != -1:
            # If memory table already has that entry calculated, use it.
            return t[n][W]

        # Get rid of last item because weight of item is greater
        # than the W itself.
        if wt[n - 1] > W:
            # Advance in recursion without last item.
            # but store the results in the memory table.
            t[n][W] = helper_memoize(wt, val, W, n - 1)
            return t[n][W]
        else:
            # Weight of last item is within W, thus, 2 possibilities are there:
            # max(consider item, not consider item)
            # store the results in memory table.
            t[n][W] = max(val[n - 1] + helper_memoize(wt, val, W - wt[n - 1], n - 1),
                          helper_memoize(wt, val, W, n - 1))

            return t[n][W]

    return helper_memoize(wt, val, W, n)


def knapsack_dp(wt, val, W):
    n = len(wt)

    # DP One line initialization.
    t = [[0 if i == 0 or j == 0 else -1 for j in range(W+1)] for i in range(n+1)]

    # Because initialization is already done for n = 0, W = 0.
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                # Convert n to i and W to j from recursive solution.
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i - 1][j]

            pprint(t)

    return t[n][W]


def subset_sum(A, S):
    n = len(A)

    t = [[1 if j == 0 else 0 for j in range(S+1)] for i in range(n+1)]

    pprint(t)

    for i in range(1, n+1):
        for j in range(1, S+1):
            if A[i-1] <= j:
                t[i][j] = t[i-1][j - A[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    pprint(t)
    return t[n][S]


if __name__ == '__main__':
    # wt = [1, 4, 5, 7]
    # val = [3, 4, 5, 7]
    # W = 10
    #
    # print(knapsack_dp(wt, val, W))

    A = [1, 3, 8, 10]
    S = 9
    print(subset_sum(A, S))
