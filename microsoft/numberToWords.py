""" 
273. Integer to English Words


Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 2^31 - 1


solution:

0 : Zero
to19 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thous = ["Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]

"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        to19 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Eleven","Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty","Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thous = ["Thousand", "Million", "Billion", "Trillion", "Quadrillion",
                 "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
        
        def recusor(number: int) -> str:
            if number == 0: return ""
            
            if number <20: return to19[number-1]
            
            if number < 100: return (tens[number//10 -2] + " " + to19[number%10-1]).rstrip()
            
            if number < 1000:
                return (recusor(number//100) + " Hundred " + recusor(number%100)).rstrip()
            
            if number < 10**6:
                return (recusor(number//10**3) + " Thousand " + recusor(number % 10**3)).rstrip()
            
            if number < 10**9:
                return (recusor(number//10**6) + " Million " + recusor(number % 10**6)).rstrip()
            
            return (recusor(number//10**9) + " Billion " + recusor(number % 10**9)).rstrip()
            
        
        
        return recusor(num)
    
    
def test_func():
    solution = Solution()
    print(solution.numberToWords(123456789))
    
test_func()