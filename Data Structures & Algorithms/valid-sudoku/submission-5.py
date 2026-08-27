class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, square = [0] * 9, [0] * 9, [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                val = int(val) - 1

                if (1 << val) & row[r]:
                    return False
                if (1 << val) & column[c]:
                    return False
                if (1 << val) & square[(r//3) * 3 + (c//3)]:
                    return False
                
                row[r] |= (1 << val)
                column[c] |= (1 << val)
                square[(r//3) * 3 + (c//3)] |= (1 << val)

        return True