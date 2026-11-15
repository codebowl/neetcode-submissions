class Solution:
    def is_valid(self, values: list[str]) -> bool:
        nums = [0] * 9
        for s in values:
            if s != ".":
                d = int(s)
                if d < 0 or d > 9 or nums[d-1] != 0:
                    return False
                nums[d-1] += 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            if not self.is_valid(r):
                return False
        
        for c in range(9):
            column = [r[c] for r in board]
            if not self.is_valid(column):
                return False

        for i_c in range(3):
            for i_r in range(3):
                c_s = i_c * 3
                c_e = c_s + 3
                r_s = i_r * 3
                r_e = r_s + 3
                print(c_s, c_e, r_s, r_e)
                box = [i for row in board[r_s:r_e] for i in row[c_s:c_e]]
                if not self.is_valid(box):
                    return False
        
        return True