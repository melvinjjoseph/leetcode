class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols= len(board), len(board[0])
        
        def dfs(r,c):
            if r==rows or c==cols or r<0 or c<0 or board[r][c]=="T" or board[r][c]=="X":
                return 
            board[r][c]="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"
        
        
        