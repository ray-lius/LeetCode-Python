"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45


Solution:
1, how to get Nth stair, from n-1 stair, or from n-2 stair
2, 

"""

#O(n)
def climbStairs(n: int)->int:
    dp = {}
    dp[0] = 1
    dp[1] = 1
    idx = 2
    while idx <= n:
        dp[idx] = dp[idx-1] + dp[idx-2]
        idx += 1
    return dp[n]

testCase = [2,3,5]
print ( [ climbStairs(i) for i in testCase])
# expect 2, 3, 8



"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

recursions / fab
Solution 1:
maxMoney[n]  =  nums[n] + maxMoney[n-2] / maxMoney[n-1]

Solution 2:
use variable to store tmp value
use curMax = max(curMax, preMax)


Solution 3:
use variable to store tmp value
a: to store the odd number
b: to store the even number
a = max(a+nums[idx], b)
b=  max(b+nums[idx], a)


"""
def robMoney(nums: list[int])->int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[1], nums[0])
    
    dp = {}
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    idx = 2
    length = len(nums)
    while idx < length:
        dp[idx] = max(nums[idx] + dp[idx-2], dp[idx-1])
        idx += 1
    return dp[length-1]

def robMoney2(nums: list[int])->int:
    length = len(nums)
    if( length == 0):
        return 0
    curMax = 0
    preMax = 0
    idx = 0
    while idx < length:
        tmp = curMax
        curMax = max(curMax, nums[idx]+preMax)
        preMax = tmp
        idx += 1
    return curMax


def robMoney3(nums: list[int])->int:
    length = len(nums)
    oddMax = 0
    evenMax = 0
    idx = 0
    while idx < length:
        if idx%2 == 0 :
            evenMax = max(evenMax+nums[idx], oddMax)
        else:
            oddMax = max(evenMax, oddMax+nums[idx])
        idx += 1
    return max(oddMax, evenMax)



testCases = [[1,2,3,1],[2,7,9,3,1], [1,3,1,3,100] ]
print([robMoney(i) for i in testCases ])
print([robMoney2(i) for i in testCases])
print([robMoney3(i) for i in testCases])





"""
you are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


solution: (greedy)
1) sort the coins to increase order
2) get the reminder for each coin

bad solution, not feasible !!!!!!

DFS - back tracking

solution2:
1) dp = []



"""

def coinChange(coins: list[int], amount: int)->int:
    # if amount  == 0:
    #     return 0
    
    # count  = 0
    # coins = sorted(coins, reverse=True)
    # for coin in coins:
    #     if coin > amount:
    #         continue
    #     elif coin == amount:
    #         count  += 1
    #         amount  = 0
    #     else:
    #         count  += amount//coin
    #         amount = amount%coin
        
    #     print(coins, coin, amount, count)
    #     if amount == 0:
    #         break

    # if amount != 0:
    #     return -1

    # return count

    dp = [amount + 1]*(amount+1)
    dp[0] = 0

    for i in range(1, amount+1, 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i-coin]+1, dp[i])
            else:
                continue

    return dp[amount] if dp[amount] != amount + 1 else -1


testCases = [[[1,2,5], 11], [[2], 3], [[1],0], [[1,3,4,5], 7], [[186,419,83,408], 6249]]
print([coinChange(val[0], val[1]) for val in testCases])







