"""
MATH:







"""

def plusOne( digits: list[int]) -> list[int]:
    if digits[-1] == 9 :
        digits[-1] = 0

        return [1] + digits
    else :
        digits[-1] += 1
        return digits


def plusOne2(digits: list[int]) -> list[int]:

        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                print(digits, i)
                digits[i]+=1
                return digits
        print(digits)
        return [1]+digits


test_cases = [[1,2,3], [9,4,0,2], [9,9,9]]
print( [ plusOne(test) for test in test_cases])
print( [ plusOne2(test) for test in test_cases])