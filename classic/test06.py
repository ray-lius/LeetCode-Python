"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


solution 1: DP problem
1. find the first string, and get the position
need review 


"""
# def wordBreak( s: str, wordDict: list[str]) -> bool:
#         wordset=set(wordDict)
#         n=len(s)
#         dp=[False]*(n+1)
#         dp[n]=True
#         for ind1 in range(n-1,-1,-1):
#             for end in range(ind1+1,n+1):
#                 word=s[ind1:end]
#                 print(ind1, end, word, dp, wordDict )
#                 if word in wordset and dp[end]:
#                     dp[ind1]=True
#                     break
#         return dp[0]


# def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     dp = [False] * (len(s) + 1)
#     dp[0] = True
#     min_len, max_len = min(map(len, wordDict)), max(map(len, wordDict))

#     for i in range(len(s)):
#         for j in range(i + min_len, min(len(s), i + max_len + 1) + 1):
#             if dp[i] and s[i:j] in wordDict:
#                 dp[j] = True
#                 #break
#     return dp[len(s)]



# def wordBreak(s: str, wordDict: list[str])->bool:
#     length =  len(wordDict)
#     pos = 0
#     for val in wordDict:
#         s = s[pos:]
#         pos = s.find(val)
#         if pos == -1:
#             return False
#         else:
#             pos = pos + len(val)

#     return True

def wordBreak(s: str, wordDict: list[str])->bool:

    dp = [False]*(len(s)+1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i + len(w))<=len(s) and s[i : i+len(w)] == w:
                dp [i] = dp [i + len(w)]
            if dp[i]:
                break
    return dp[0]


testCases = [["leetcode", ["leet","code"]], ["applepenapple", ["apple","pen"]], ["bb", ["a","b","bbb","bbbb"]]]
#print(wordBreak("leetcode", ["leet","code"]))
print([wordBreak(val[0], val[1]) for val in testCases])







"""

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.


"""

def simplify(path: str)->str:
    path_arr = path.split("/")
    path_len = len(path)
    result = []
    for each in path_arr:
        if each == "..":
            if len(result) > 0:
                result.pop()
        elif each != "."  and len(each) > 0:
            result.append(each)
    print(result)
    if len(result) == 0:
        return "/"
    res_str = '/'.join(result)
    return "/"+res_str



testCases = ["/home/", "/../", "/home//foo/"]
print([simplify(i) for i in testCases])