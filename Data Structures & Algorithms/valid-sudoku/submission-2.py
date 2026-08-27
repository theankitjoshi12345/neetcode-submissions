class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        return False
            seen = set()

        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        return False
            seen = set()


        seen1 = set()
        seen2 = set()
        seen3 = set()
        for i in range(9):
            for j in range(0, 3):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in seen1:
                    return False
                else:
                    seen1.add(board[i][j])
            for j in range(3, 6):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in seen2:
                    return False
                else:
                    seen2.add(board[i][j])
            for j in range(6, 9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in seen3:
                    return False
                else:
                    seen3.add(board[i][j])
            if (i+1)%3 == 0:
                seen1 = set()
                seen2 = set()
                seen3 = set()

        return True