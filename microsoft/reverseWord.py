"""186. Reverse Words in a String II

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
 

Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.

 """


class Solution:
    def reverseWords(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(''.join(s).split(' ')[::-1])
        print(' '.join(''.join(s).split(' ')[::-1]))
        s[:] = list(' '.join(''.join(s).split(' ')[::-1]))
    
    def reverseWords2(self, s: list[str]) -> None:
        # first rever all str, O(n)
        s[:] = s[::-1]
        # find each word and then reverse again
        start = 0
        for idx, val in enumerate(s):
            if val == " ":
                s[start:idx] = s[start:idx][::-1]
                start = idx + 1
            if idx == len(s)-1:
                s[start:idx+1] = s[start:idx+1][::-1]
        print(s)
        

def test_reverseWords():
    solution = Solution()

    # Test case 1
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    solution.reverseWords2(s)
    print(s)
    assert s == ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

    # Test case 2
    s = ["a"]
    solution.reverseWords(s)
    assert s == ["a"]

test_reverseWords()
        



