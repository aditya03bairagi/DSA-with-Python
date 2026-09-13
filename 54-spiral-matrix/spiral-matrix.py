class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)  # total number of rows
        n = len(matrix[0]) # total number of columns

        total = m * n   # total elements in matrix, e.g. 3 * 3 = 9 elements

        ans = []
        c = 0       # counter variable

        col_start = 0
        row_start = 0
        col_end = n - 1
        row_end = m - 1

        while c < total:
            # rowstart: colstart -> colend
            for i in range(col_start, col_end + 1):
                ans.append(matrix[row_start][i])
                c += 1
            row_start += 1

            if c == total:
                break
            
            # colend: rowstart -> rowend
            for i in range(row_start, row_end + 1):
                ans.append(matrix[i][col_end])
                c += 1
            col_end -= 1

            if c == total:
                break

            # rowend: colend -> colstart
            for i in range(col_end, col_start - 1, -1):
                ans.append(matrix[row_end][i])
                c += 1
            row_end -= 1

            if c == total:
                break

            # colstart: rowend -> rowstart
            for i in range(row_end, row_start - 1, -1):
                ans.append(matrix[i][col_start])
                c += 1
            col_start += 1

        return ans