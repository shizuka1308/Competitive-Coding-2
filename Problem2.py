# Time Complexity:O(n×c), where n is the number of items and c is the knapsack capacity, as each subproblem is 
# solved once and stored in the DP table.
# Space Complexity: O(n×c) due to the memoization table storing results for all subproblems.
# Used memoization (top-down DP) to solve the 0/1 knapsack problem by recursively exploring both inclusion and exclusion 
# of each item while storing results in a DP table to avoid redundant calculations. 
# If a subproblem is already computed, it directly returns the stored value, optimizing time complexity.
def knapsack_memo(c, wt, val, n, dp):
    # base case
    if c==0 or n==0:
        return 0
    # found the value in my dp
    if dp[c][n] != -1:
        return dp[c][n]
    # cannot have wt greater than the given capacity 
    if wt[n-1] > c:
        dp[c][n] = knapsack_memo(c, wt, val, n-1, dp)
    else:
        include = val[n-1] + knapsack_memo(c - wt[n-1], wt, val, n-1, dp)
        exclude = knapsack_memo(c, wt, val, n-1, dp)
        dp[c][n] = max(include, exclude)
    return dp[c][n]


wt = [10, 20, 30]
val = [60, 100, 120]
capacity = 50
n = len(val)
dp = [[-1 for _ in range(n + 1)] for _ in range(capacity + 1)]
print(knapsack_memo(capacity, wt, val, n, dp))