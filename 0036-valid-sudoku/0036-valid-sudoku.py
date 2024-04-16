class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sub = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if board[i][j] != '.':
                    k = (i // 3) * 3 + j //3

                    if curr not in rows[i]:
                        rows[i].add(curr)
                    else:
                        return False
                    
                    if curr not in cols[j]:
                        cols[j].add(curr)
                    else:
                        return False
                    if curr not in sub[k]:
                        sub[k].add(curr)
                    else:
                        return False
        return True

