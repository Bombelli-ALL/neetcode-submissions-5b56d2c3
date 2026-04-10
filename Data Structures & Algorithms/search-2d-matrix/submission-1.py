class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        start, end  = 0,  ROWS - 1
        while start <= end:
            m = start + ((end - start) // 2)
            if matrix[m][-1] < target:
                start = m + 1
            elif matrix[m][0] > target:
                end = m - 1
            else:
                a, r = 0, COLS - 1
                while a <= r:
                    n = a + ((r - a) // 2)
                    if matrix[m][n] < target:
                        a = n + 1
                    elif matrix[m][n] > target:
                        r = n - 1
                    else:
                        return True
                return False
        if not start <= end:
            return False