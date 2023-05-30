'''
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                 "XC": 90, "L": 50, "XL": 40, "X": 10, "V": 5, "IV": 4, "I": 1}
        i = 0
        integer = 0

        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman:
                integer += roman[s[i:i+2]]
                i += 2
            else:
                # print(integer)
                integer += roman[s[i]]
                i += 1
        return integer


s = input('Enter Roman Number: ')
obj = Solution()
print('Integer Number: ', obj.romanToInt(s))
