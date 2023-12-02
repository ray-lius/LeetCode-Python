""""



"""


from collections import deque


def solution(S):
    #  brute force have run time error
    #  will check bit fo recalulation
    #  always check the last digit, if 1 mean odd, substract 1, if 0, divide 2, remove 0

    #  remove the leading 0
    for digit in S:
        if digit == '0':
            S = S[1:]
        else:
            break

    print(S)
    def recursor(value, times):
        if value == "0":
            return times

        print(value)
        if value[-1] == "1":
            value = value[:-1] + "0"
            return recursor(value, times+1)
        else:
            value = value[:-1]
            return recursor(value, times+1)

    return recursor(S, 0)


# print(solution("011100"))
# print("000011100".lstrip("0"))

# stack = deque([1,2,3])

# print(stack.pop() - stack.pop())
# print(stack)
# stack.pop()
# print(stack)

# if stack:
#     print("kkkkk")
# else:
#     print(0)


def solution2(S):

    stack = deque([])  # store stack value in order
    operations = S.split(" ")

    for operation in operations:

        print(stack)
        if operation == "POP":
            if len(stack) == 0:
                return -1
            stack.pop()

        elif operation == "DUP":
            if len(stack) == 0:
                return -1
            stack.append(stack[-1])

        elif operation == "+":
            if len(stack) == 1:
                return -1
            result = stack.pop()+stack.pop()
            if result > 2**20-1:
                return -1
            stack.append(result)

        elif operation == "-":
            if len(stack) == 1:
                return -1
            result = stack.pop()-stack.pop()
            if result < 0:
                return -1
            stack.append(result)

        elif operation.isnumeric():  # input interger
            X = int(operation)
            if X > 2**20-1 or X < 0:
                return -1
            stack.append(int(operation))

        else:  # unknown input
            return -1

    return stack[-1]


print(solution2('4 5 6 - 7 +'))
