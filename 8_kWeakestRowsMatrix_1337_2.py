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

https://tutorialcup.com/wp-content/uploads/2020/10/Screenshot-from-2020-10-22-16-54-45.png
'''


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soilder = 0
        soilder_lst = []
        result = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 1:
                    soilder += 1
            soilder_lst.append(soilder)
            soilder = 0
        # The number of soldiers in each row from weakest to strongest
        print(soilder_lst)

        # return index of sorted list
        row = len(soilder_lst)
        index_result = []
        for m in range(0, row):
            result.append(soilder_lst[m] * row + m)
        print(result)
        result.sort()
        for n in range(0, k):
            index_result.append(result[n] % row)
        return index_result


# matrix ,k = input('Enter matrix: '),input('Enter k: ')
# matrix_print = np.matrix(matrix)
matrix = [[1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]]
k = 3

mat2 = [[1, 0], [1, 0], [1, 0], [1, 1]]
k2 = 4

mat3 = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k3 = 3

mat4 = [[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]]
k4 = 2
obj = Solution()
print('k1')
print(obj.kWeakestRows(matrix, k))
print('k2')
print(obj.kWeakestRows(mat2, k2))
print('k3')
print(obj.kWeakestRows(mat3, k3))
print('k4')
print(obj.kWeakestRows(mat4, k4))
