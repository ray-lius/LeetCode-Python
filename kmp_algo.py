"""
kmp alogorithm:


input: “AABAACAADAABAABA”
patt : “AABA”

input : "ABAABABABCA"
patt : "ABABC"


solution:
search patt in the string, and get the index value of the patt first index

"""


def build_next(patt: str)->list[int]:
    """
    calculate NEXT list
    """
    next = [0]
    prefix_len = 0
    i = 1
    while i < len(patt):
        if patt[prefix_len] == patt[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len-1]
    return next

def kmp_search(string: str, patt: str)->int:

    next = build_next(patt)
    print(next)
    i = 0
    j = 0
    while i < len(string):
        if(string[i] == patt[j]):
            i += 1
            j += 1
        elif j > 0:
            j = next[j-1]
        else:
            i += 1

        if j == len(patt):
            print(i, j)
            return i - j
        
    return -1    
    

testCases = [["ABAABABABCA", "AABA"], ["ABAABABABCA","ABABC" ]]

print([kmp_search(val[0], val[1]) for val in testCases])
