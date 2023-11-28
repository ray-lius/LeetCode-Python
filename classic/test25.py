"""
208 Implement Trie (prefix tree) used for such as autocomplete and spellchecker.

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.


"""

# cause 
from collections import defaultdict


class Trie:

    def __init__(self):
        self.words = []
        

    def insert(self, word: str) -> None:
        self.words.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False
    


class Trie2:

    def __init__(self):
        self.words = []
        self.dict = defaultdict()
        

    def insert(self, word: str) -> None:
        self.words.append(word)
        n = len(word)
        for i in range(n):
            self.dict[word[:i+1]] = 1

        

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.dict:
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


"""

211 Design Add and search words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.


"""

class WordDictionary:

    def __init__(self):
        self.d={}
        
    def addWord(self, word: str) -> None:
        cur=self.d
        if not self.search(word):
            for i in range(len(word)):
                if word[i] not in cur:
                    cur[word[i]]={}
                cur=cur[word[i]]
                
            cur["#"]={}  
        print(self.d)  
        

    def search(self, word: str) -> bool:
        cur=self.d
        def rec(start,cur):
            if start>=len(word):
                if "#" in cur:
                    return True
                else:
                    return False
                
            if word[start]==".":
                for k,v in cur.items():
                    if rec(start+1,v):
                        return True
                return False
            elif word[start] in cur:
                if rec(start+1,cur[word[start]]):
                    return True
                
            else:
                return False
            
        return rec(0,cur)  
        
# wrong way !!!!!! will cause time out !!!!!!!!
class WordDictionary2:

    def __init__(self):
        self.words = {}
        

    def addWord(self, word: str) -> None:
        if word not in self.words:
            self.words.append(word)


    @staticmethod
    def compare_two_word(word1: str, word2: str)->bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        for idx in range(n1):
            if word2[idx] != "." and word1[idx] != word2[idx]:
                return False
        return True

    def search(self, word: str) -> bool:
        for each in self.words:
            if self.compare_two_word(each, word):
                return True
        return False
    

    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


wordDictionary = WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
res1 = wordDictionary.search("pad"); 
res2 = wordDictionary.search("bad"); 
res3 = wordDictionary.search(".ad"); 
res4 = wordDictionary.search("b.."); 


print(res1,res2,res3, res4)


"""

79. Word Search

Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true


example2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

example3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def exist(board: list[list[str]], word: str)->bool:
    visited = [ [] for _ in board]
    for i in visited:
        visited[i] = [ False for _ in board[0]]
    
    for i in board:
        for j in board[i]:
            if search_word(board, word, visited, 0, i, j):
                return True
            
    return False

def is_in_board(board: list[list[str]], x: int, y: int)->bool:
    return x>=0 and x<len(board) and y>=0 and y<len(board[0])

def search_word(board: list[list[str]], word: str, visited: list[list[bool]], index: int, x: int, y : int)->bool:
    if index == len(word)-1:
        return board[x][y] == word[index]
    if board[x][y] == word[index]:
        visited[x][y] = True
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if is_in_board(board, nx, ny) and not visited[nx][ny] and search_word(board, word, visited, index+1, nx, ny):
                return True
        visited[x][y] = False
    return False



"""
212. Word Search II

Companies
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]


example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

"""

def exist_words(board: list[list[str]], words: list[str])->list[str]:
    result = []
    for word in words:
        if exist(board, word):
            result.append(word)
    return result