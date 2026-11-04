class Solution:
    EMPTY = "."  

    def is_valid(self, nums: list[str]) -> bool:
        options = [0] * 9
        for n in nums:
            if n == self.EMPTY:
                continue

            num_index = int(n) - 1
            exists = options[num_index] != 0
            if exists:
                return False
            
            options[num_index] += 1

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate row
        for row in board:
            v = self.is_valid(row)
            if v is False:
                return False

        # validate column
        for column in range(9):
            nums = [v[column] for v in board]
            v = self.is_valid(nums)
            if v is False:
                return False

        # validate 3x3 box
        column_shift = 3
        values = []
        for column in range(3):
            for row in range(9):
                if row % 3 == 0 and len(values) > 0:
                    is_valid = self.is_valid(values)
                    if not is_valid:
                        return False
                    values = []
                column_start = column * column_shift
                segment = board[row][column_start:column_start + 3]
                values += segment
        
        return True
