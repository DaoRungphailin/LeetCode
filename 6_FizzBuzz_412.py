'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_list = []
        for i in range(1, int(n)+1):
            if i % 3 == 0 and i % 5 == 0:
                result_list.append("FizzBuzz")
            elif i % 3 == 0:
                result_list.append("Fizz")
            elif i % 5 == 0:
                result_list.append("Buzz")
            else:
                result_list.append(str(i))
        # return (str(result_list).replace("'",'"').replace(' ',''))
        return result_list


# Driver Code
obj = Solution()
n = input('Enter 1 Number: ')
print(obj.fizzBuzz(n))