# 官网的代码真的简单，我写的好复杂
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        ans = [[0] * n for _ in range(n)]
        i = 0
        j = 0
        ans[i][j] = num
        while 1:
            right = True
            up = True
            left = True
            down = True
            if (j + 1) > (n - 1):
                right = False
            elif ans[i][j + 1] != 0:
                right = False

            if (i - 1) < (0):
                up = False
            elif ans[i - 1][j] != 0:
                up = False

            if (i + 1) > (n - 1):
                down = False
            elif ans[i + 1][j] != 0:
                down = False

            if (j - 1) < 0:
                left = False
            elif ans[i][j - 1] != 0:
                left = False

            if (not right) and (not up) and (not left) and (not down):
                return ans

            while (j + 1) <= (n - 1) and ans[i][j + 1] == 0:
                j += 1
                num += 1
                ans[i][j] = num
            while (i + 1) <= (n - 1) and ans[i + 1][j] == 0:
                i += 1
                num += 1
                ans[i][j] = num
            while (j - 1) >= 0 and ans[i][j - 1] == 0:
                j -= 1
                num += 1
                ans[i][j] = num
            while (i - 1) >= 0 and ans[i - 1][j] == 0:
                i -= 1
                num += 1
                ans[i][j] = num
        return ans


class Solution_official:
    def generateMatrix(self, n: int):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4   # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy
        
        return matrix