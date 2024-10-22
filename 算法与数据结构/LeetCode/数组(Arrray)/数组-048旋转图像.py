""" 048 旋转矩阵
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
] 
"""

from typing import List
class Solution:
    #my Solution
    def rotate(self, matrix: List[List[int]]) :
        matrix_len = len(matrix) #get martix dims
        for i in range(0,matrix_len//2): # operate the image by each ixi outside edge
            #[i,matrix-i)
            for j in  range(i,matrix_len-i-1):
                value1 = matrix[j][matrix_len-1-i]
                matrix[j][matrix_len-1-i] = matrix[i][j]
                value2 = matrix[matrix_len-1-i][matrix_len-1-j]
                matrix[matrix_len-1-i][matrix_len-1-j] = value1
                value1 = matrix[matrix_len-1-j][i]
                matrix[matrix_len-1-j][i] = value2
                matrix[i][j] = value1
        return matrix

test = Solution()
print (test.rotate([[1,2,3],[4,5,6],[7,8,9]]))



