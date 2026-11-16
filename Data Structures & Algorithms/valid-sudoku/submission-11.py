class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                d = int(v) - 1
                mask = 1 << d
                square_key = (r//3) * 3 + (c//3)
                if (mask & rows[r]) or (mask & cols[c]) or (mask & squares[square_key]):
                    return False
                rows[r] |= mask
                cols[c] |= mask
                squares[square_key] |= mask
        return True