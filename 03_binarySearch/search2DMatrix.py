class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = n*m-1
        while start <= end:
            middle = start + (end-start) // 2
            holder = matrix[middle//n][middle%n]
            if holder == target:
                return True
            elif holder < target:
                start += 1
            else:
                end -= 1
        return False
    
if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print (sol.searchMatrix (matrix, target))