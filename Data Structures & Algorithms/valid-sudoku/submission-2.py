class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        countcol = [set() for _ in range(n)]
        countbox = [set() for _ in range(n)]
        countrow = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num != ".":
                    box_index = 3*(i // 3) + j // 3
                    if num in countrow[i]:
                        return False
                    else: 
                        countrow[i].add(num)
                    if num in countcol[j]:
                        return False
                    else:
                        countcol[j].add(num)
                    if num in countbox[box_index]:
                        return False
                    else:
                        countbox[box_index].add(num)
        return True



            
        