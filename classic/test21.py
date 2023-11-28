"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104



"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
        
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        print (sorted_intervals)
        result = []

        for interval in sorted_intervals:
            print(result, interval[0], sorted_intervals[-1][1]), 
            if not bool(result) or (interval[0] > result[-1][1]):
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

def another(s: str)->bool:
     pass

testCases =[[[1,3],[2,6],[8,10],[15,18]] , [[1,4],[4,5]], [[1,4],[0,4]]]
print([merge(i) for i in testCases])