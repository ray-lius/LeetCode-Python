"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


solution 1:
for each in strs, 
   sort()
build array = []

if val in array, 
    check the array, if has, then group
    if not, add a new arrray


"""

from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for i in t:
        if i not in dict:
            return False
        else:
            dict[i] -= 1

    for each in dict:
        if dict[each] != 0:
            return False
    return True

def groupAnagram(strs: list[str])->list[list[str]]:
    result = []
    dict = {  }
    for  val in strs:
        isGrouped = False
        for each in dict:
            if isAnagram(each, val):
                dict[each].append(val)
                isGrouped = True
                break
        if not isGrouped:
            dict[val] = [val]
    
    for each in dict:
        result.append(dict[each])

    return result

def groupAnagram2(strs: list[str])->list[list[str]]:
    dict = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        dict[sorted_word].append(word)

    return list(dict.values())
        

testCases =[["eat","tea","tan","ate","nat","bat"] ]
print([groupAnagram(i) for i in testCases])
print([groupAnagram2(i) for i in testCases])

word = 'dish'
print(sorted(word))

testArr01 = [2,2,2,3,8,3,4]
print(max(testArr01, key=testArr01.count))
print(max(set(testArr01), key=testArr01.count))

teststr01 = 'aaabbc'
print(max(teststr01, key=teststr01.count))
print(set(teststr01))
print(max(set(teststr01), key=teststr01.count))
        
