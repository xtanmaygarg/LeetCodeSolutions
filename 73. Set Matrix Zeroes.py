class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if matrix == [[]]:
            return [[]]
        rowZero = False
        colZero = False
        row = len(matrix)
        col = len(matrix[0])
        
        if 0 in matrix[0]:
            rowZero = True
        
        for i in range(row):
            if matrix[i][0] == 0:
                colZero = True
                break
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, col):
            if matrix[0][i] == 0:
                for rows in range(1, row):
                    matrix[rows][i] = 0
        
        for i in range(1, row):
            if matrix[i][0] == 0:
                for cols in range(1, col):
                    matrix[i][cols] = 0
        
        if rowZero:
            for i in range(col):
                matrix[0][i] = 0
        
        if colZero:
            for i in range(row):
                matrix[i][0] = 0
        
        return matrix
