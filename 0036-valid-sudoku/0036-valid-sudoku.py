class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        blockMap = defaultdict(set)

        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in rowMap[i] or board[i][j] in colMap[j] or board[i][j] in blockMap[(i // 3, j // 3)]:
                        return False
                    else:
                        rowMap[i].add(board[i][j])
                        colMap[j].add(board[i][j])
                        blockMap[(i // 3, j // 3)].add(board[i][j])
        return True