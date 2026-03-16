# similar to string matching concepts not pick not pick subsequence bs

def exist(self, board: List[List[str]], word: str) -> bool:
    n = len(board)
    m = len(board[0])
    def f(i, j, k):
        if k == len(word):
            
            return True
        if i >= n or j >= m or i < 0 or j < 0:
            return False
        if board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        up = f(i-1, j,k+1)
        right = f(i+1, j,k+1)
        down = f(i, j+1,k+1)
        left = f(i, j-1,k+1)
        board[i][j] = temp
        return down or right or left or up
    for i in range(n):
        for j in range(m):
            if f(i, j, 0):
                return True

    return False

