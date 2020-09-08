#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque

        if not image:return[]
        if not image[0]:return[]

        rows = len(image)
        cols = len(image[0])


        color = image[sr][sc]
        if color == newColor:
            return image
            
        quque = deque()
        quque.append((sr,sc))

        while quque:
            pixel = quque.popleft()
            image[pixel[0]][pixel[1]] =  newColor
            for di,dj in {(1,0),(0,1),(-1,0),(0,-1)}:
                row = di + pixel[0]
                col = dj + pixel[1]
                if 0 <= row < rows and 0<=col < cols and image[row][col] == color:
                    quque.append((row,col))
        
        return image
# @lc code=end

