class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for ele in board:
            for i in range(0, len(ele)):
                if ele[i] != ".":
                    ele[i] = int(ele[i])
                else:
                    ele[i] = 0
        tmp: list[int] = []
        for ele in board:
            for i in ele:
                if i != 0:
                    if i not in tmp:
                        tmp.append(i)
                    else:
                        return False
            tmp = []
        for n in range(0, len(board)):
            for ele in board:
                if ele[n] != 0:
                    if ele[n] not in tmp:
                        tmp.append(ele[n])
                    else:
                        return False
            tmp = []
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val != 0:
                            if val not in tmp:
                                tmp.append(val)
                            else:
                                return False
                tmp = []
        return True