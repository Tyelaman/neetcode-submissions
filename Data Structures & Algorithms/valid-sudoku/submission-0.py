class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                
                val = board[r][c]
                if val != ".":
                    row_marker = (r, val)
                    col_marker = (val, c)
                    box_marker = (r // 3, c // 3, val)
                    
                    if row_marker in seen or col_marker in seen or box_marker in seen:
                        return False

                    seen.update([row_marker, col_marker, box_marker])
        return True