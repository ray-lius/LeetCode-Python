"""

BACK TRACKING


17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Question 



Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]



solution 1:

use permutation
dict = {}
for each in digits: use permutation.....

"""


from itertools import permutations
import itertools


def letterCombination(digits: str)->list[str]:
    letter_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y','z'],
    }
    
    # digits_len = len(digits)
    digits_list = []
    for digit in digits:
        digits_list.append(letter_dict[digit])
        
    result = []
    
    def backtrack(comb, digits_list):
        
        
        if len(digits_list)==0:
            result.append(comb[:])
        else:
            for each in digits_list[0]:
                comb.append(each)
                backtrack(comb, digits_list[1:])
                comb.pop()

    backtrack([], digits_list)
    return result

test_cases4 = ["23"]
print("telephone combination: ", [letterCombination(test) for test in test_cases4])


#######################################################

###################################################
#####
##### there are couple ways to do the permutation!!!
#####
##################################################


## use build in function
def permute1(nums: list[int])->list[list[int]]:
    return permutations(nums)
    


def permute2(nums: list[int])->list[list[int]]:
    return [[x,y,x] for x in nums for y in nums for z in nums if x!=y and x!=z and y!=z]


print ('built in function', permute1([1,2,3]))
print ('itratable', permute2([1,2,3]))

#############################################################
###### with itertools to do the product and 
##############################################################

print('basic: ', list(itertools.permutations([1,2,3])))
print('basic: permute ', list(itertools.permutations([1,2,3], 2)))

print('basic: product', list(itertools.product([1,2,3], [4,5,6], [7,8])))

print('basic: product with repeat', list(itertools.product([1,2, 3], repeat=2)))


print("basic: combination", list(itertools.combinations('123', 2)))



# print function
def perm(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i] ,a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

perm([1,2,3])



# This is inspired by the Haskell implementation using list comprehension:
def permutation(list):
    if len(list) == 0:
        return [[]]
    else:
        return [[x] + ys for x in list for ys in permutation(delete(list, x))]

def delete(list, item):
    lc = list[:]
    lc.remove(item)
    return lc

print('Haskell implementation using list comprehension:', permutation([1,2,3]))


#############################################################################################################
"""
BACK TRACKing ways 

46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


solution 1:
back tracking
res = []

for each in nums:
    return bc(each, res, nums)

def bc:


"""


def permute(nums: list[int]):
    
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums[:]]
    
    res = []
    for i in range(len(nums)):
        
        n = nums.pop(0)
        perms = permute(nums)
    
        
        for perm in perms:
            perm.append(n)
        
        res.extend(perms)
        nums.append(n)
    
    return res
    
    
test_cases = [[1,2,3], [4,5]]
print("tets the permute", [ permute(test) for test in test_cases])



"""

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


solution:

back tracking 
dp
DFS
"""


def combinate(n: int, k: int)->list[list[int]]:
    result = []
    
    def backtrack(start: int, comb:list[int]):
        
        #base case
        if len(comb) == k:
            result.append(comb[:])
        else:
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
    
    backtrack(1, [])
    return result

test_cases2= [[4, 2], [1, 1]]

print("comnbinattion : ", [combinate(test[0], test[1]) for test in test_cases2])

jjjjj = "a"
print(jjjjj[:-1])

test_dict = {
    1: [1,2],
    2: [2,3],
    3: [1,2]
}
print(list(test_dict.keys()))
hhhhh = [[x, y] for x in list(test_dict.keys()) for y in list(test_dict.keys()) if x!=y and test_dict[x] == test_dict[y]]
tupled = set(map(tuple, hhhhh))
print( tupled)

res =[] 

a= [1,2]
b= [2,1]
a.sort()
b.sort()
a = tuple(a)
b = tuple(b)
print(a == b)

test_dict_2 = {}

for each in test_dict:
    test_dict[each].sort()
    tupled = tuple(test_dict[each])
    if tupled not in test_dict_2:
        test_dict_2[tupled] = [each]
    else:
        test_dict_2[tupled].append(each)

print([x for x in list(test_dict_2.values()) if len(x)>1])


""" 
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]




brutal force:


back tracking:

def 



"""

def isPerfect(pars: str)->bool:
    stack = []
    for each in pars:
        if each == '(':
            stack.append(each)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def generateParentheses(n: int)->list[str]:
    res = []
    
    def bt(p_str):
        if len(p_str) == 2*n:
            if isPerfect(p_str):
                res.append(p_str)
            return
        
        new_str = p_str + '('
        bt(new_str)
        new_str_2 = p_str + ')'
        bt(new_str_2)
    bt('(')
    return res


def generateParentheses2(n: int)->list[str]:
    
    stack = []
    res = []
    
    def backtrack(leftN, rightN):
        if leftN == rightN == n:
            res.append(''.join(stack))
        
        if leftN<n:
            stack.append('(')
            backtrack(leftN+1, rightN)
            stack.pop()
        
        if rightN < leftN:
            stack.append(")")
            backtrack(leftN, rightN+1)
            stack.pop()
            
        
    backtrack(0, 0)
    return res

test_cases_5 = [3]
print([generateParentheses(test) for test in test_cases_5])
print([generateParentheses2(test) for test in test_cases_5])