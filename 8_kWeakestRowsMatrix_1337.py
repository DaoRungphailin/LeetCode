'''
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soilder = 0
        soilder_lst = []  # value in dict
        key = range(k)
        l = len(mat)
        result = []
        dict = {}  # key = k , value = soilder_lst

        for i in range(l):
            for j in range(l):
                if mat[i][j] == 1:
                    soilder += 1
            soilder_lst.append(soilder)
            soilder = 0
        # The number of soldiers in each row from weakest to strongest
        print(soilder_lst)

        for i in range(l):
            dict[i] = soilder_lst[i]

        # dict = {key:value}
        ### sort dict by value ###
        sorted_dict = sorted(dict.items(), key=lambda x:x[1]) #[(2, 1), (0, 2), (3, 2), (1, 4), (4, 5)]
        
        # index of sort list
        for a,b in sorted_dict:
            result.append(a)
            
        while(len(result) > k):
            result.pop()
        return result



# matrix ,k = input('Enter matrix: '),input('Enter k: ')
# matrix_print = np.matrix(matrix)
matrix = [[1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]]
k = 3

mat = [[1,0],[1,0],[1,0],[1,1]]
kk = 4
obj = Solution()
# print(obj.kWeakestRows(matrix, k))
print(obj.kWeakestRows(mat, kk))
