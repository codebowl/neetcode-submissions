class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
         
                s_k = (r//3, c//3)
                if v in rows[r] or v in cols[c] or v in squares[s_k]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                squares[s_k].add(v)

        return True