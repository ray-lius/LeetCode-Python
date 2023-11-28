""" 
1376. Time Needed to Inform All Employees

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.



BFS plus + tuple + deque
"""


from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        # self.total = 0
        # informed = [False] * n
        # informed[headID] = True
        # #  total inform time
        # # total = informTime[headID]
        
        # def backtracking(informer):
            
        #     if not False in informed:
        #         return 
        #     self.total = informTime[informer]
        #     for idx, i in enumerate(manager):
        #         if i == informer:
        #             informed[i] = True
        #             backtracking(idx)
        
        # backtracking(headID)
        # return self.total
        relation = defaultdict(list)
        for i in range(n):
            relation[manager(i)].append(i)
        
        q = deque([(headID, 0)])
        res = 0
        while q:
            i, time = q.popleft()
            res = max(res, time)
            for emp in relation(i):
                q.append((emp, time+informTime(i)))
            
        return res    
        
        
        
    

def test_func():
    solution = Solution()
    print(solution.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]))
    print(solution.numOfMinutes(n=6, headID=2, manager=[
          2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))



test_func()
