""" 

"""


class Solution:
    def calculate(self, order, student):
        #Code here
        while order:
            if order[-1] in student:
                if order[-1] == student[-1]:
                    order = order[:-1]
                    student = student[:-1]
                else:
                    student_cur = student[-1]
                    student = student_cur + student[:-1]
            else:
                break
        return len(student)
    
    
#     10111
# 00110