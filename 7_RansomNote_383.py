'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Example :
Input: ransomNote = "fihjjjjei", magazine = "hjibagacbhadfaefdjaeaebgi"
Output: false
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        isConstruct = False
        for i in ransomNote:
            if i in magazine:
                    magazine.remove(i) #If equal remove than check next character
            else:
                return False
        return True


ransomNote, magazine = input('Enter ransomNote: '), input('Enter magazine: ')
obj = Solution()
print(obj.canConstruct(ransomNote, magazine))
