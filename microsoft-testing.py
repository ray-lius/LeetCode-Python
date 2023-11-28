""" 

"""


def areBracketsBalanced( expr):

    leftBracket = ["(", "[", "{"]
      # build a basic stack for hold
    stack = []
    for char in expr:
        if char in leftBracket:
            stack.append(char)
        elif stack and char == ")" and stack[-1] == "(" or char == "]" and stack[-1] == "[" or char == "}" and stack[-1] == "{":
                stack.pop()
        else:
                return False

    if stack:
        return False
    return True



def test_func():
    print(areBracketsBalanced("{()}[]"))
    print(areBracketsBalanced("[][(])"))
    
    s = "adddfg"
    print(s.find('ddj'))
    
test_func()
