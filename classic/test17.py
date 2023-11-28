"""
extra test 186

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]

"""


def reverseWords(s: list[str])->None:
    index = 0 
    i = 0

    length = len(s)
    while i< length:
        if s[i] == " ":
            s[index:i] = reversed(s[index:i])
            index = i+1
        i += 1
    s[index: ] = reversed(s[index: ])
    s.reverse()


s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s[11:] = reversed(s[11:])

print(s)
print(s[12:14])

str = " the sky is blue"

print(str.split()[::-1])

print(str.split())

ll = str.split()
ll.sort()

print(ll)

arr = [1,1,2,3]
arr.remove(1)
print(arr)

s = 'ahah'
