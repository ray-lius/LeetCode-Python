""" 
Given N students, M colleges and Boolean matrix Applied[][] of N rows and M columns which represents whether the student has applied in a college or not, if Applied[i][j] is 1 then the i^th student has applied in the j^th college, otherwise not. 
Given the array No_of_seats[] where No_of_seats[i] represents the number of available seats for admission in the i^th college, What are the maximum possible admissions that could be given in total.

Note: Each student can take admission in only one college.

Example 1:

Input:
N = 3
M = 4
applied[][]=
[
[0 1 0 0],
[1 1 1 1],
[0 1 0 0],
]
no_of_seats[] = {1, 1, 1, 2}

Output: 2

Explanation: There can be maximum two admissions. Let, Student-0 take admission in college-1 and Student-1 take admission in college-0. There is no more seat available for Student-2.


"""
def max_admissions(N, M, applied, no_of_seats):
    # Create a list of tuples where each tuple contains the number of seats and the index of the college
    colleges = sorted([(seats, i) for i, seats in enumerate(no_of_seats)], reverse=True)
    
    # Initialize the count of admissions to 0
    admissions = 0
    
    # Iterate over the colleges in descending order of the number of seats
    for seats, college in colleges:
        # Iterate over the students
        for student in range(N):
            # If the student has applied to the college and there are seats available, increment the count of admissions
            if applied[student][college] == 1 and seats > 0:
                admissions += 1
                # Decrement the number of seats in the college
                seats -= 1
                # Break the loop as the student can take admission in only one college
                break
    
    return admissions

def max_admissions(N, M, applied, no_of_seats):
    def backtrack(student, seats_left, admissions):
        # If all students have been considered, return the number of admissions
        if student == N:
            return admissions
        # If not, initialize the maximum admissions to the current number of admissions
        max_admissions = admissions
        # Iterate over all colleges
        for college in range(M):
            # If the student has applied to the college and there are seats left, try admitting the student
            if applied[student][college] == 1 and seats_left[college] > 0:
                # Decrement the number of seats left in the college
                seats_left[college] -= 1
                # Recursively call the function for the next student and update the maximum admissions
                max_admissions = max(max_admissions, backtrack(student + 1, seats_left, admissions + 1))
                # Increment the number of seats left in the college (backtrack)
                seats_left[college] += 1
        # Return the maximum admissions
        return max_admissions

    # Call the function for the first student with the initial number of seats and admissions
    return backtrack(0, no_of_seats, 0)



def admission3(N, M, applied, no_of_seats):
    
    def backtracking(student: int, no_of_seats: list[int], admission: int) -> int:
        
        if student == N:
            return admission
        
        max_admissions = admission
        for college in range(M):
            if applied[student][college] == 1 and no_of_seats[college] > 0:
                no_of_seats[college] -= 1
                max_admissions = max(max_admissions, backtracking(student+1, no_of_seats, admission+1))
                no_of_seats[college] += 1
        return max_admissions
            
    
    return backtracking(0, no_of_seats, 0)

def test_func():
    N = 3
    M = 4
    applied = [
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]
    no_of_seats = [1, 1, 1, 2]
    
    print(admission3(N,M, applied, no_of_seats))
    print(max_admissions(N, M, applied, no_of_seats))
    
test_func()
