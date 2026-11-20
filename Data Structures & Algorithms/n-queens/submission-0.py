class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def backtrack(row: int, column: List[int]):
            if len(column) == n:
                solution = []
                for i in range(n):
                    string = ""
                    for j in range(n):
                        if j == column[i]:
                            string = string + "Q"
                        else:
                            string = string + "."
                    solution.append(string)
                result.append(solution)
                return

            for col in range(n):
                if (col in column):
                    continue # to next column
                
                conflict = False
                for prev_row, prev_col in enumerate(column):
                    if abs(row - prev_row) == abs(col - prev_col): #diagonal cond.
                        conflict = True
                        break
                if conflict:
                    continue

                column.append(col)
                backtrack(row + 1, column)
                column.pop()

        backtrack(0, [])
        return result

