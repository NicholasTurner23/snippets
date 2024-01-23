"""
Given an m * n grid of characters board and a string word, return true if word exists in the grid.

Thhe word can be constructed from letters sequentially adjacent cells, where adjacent cells are horizontally or vertically neighbouring. The same letter cell may not be usesd more than once.

"""
from typing import List, Set

class Solution:
    def exists(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path: Set[str] = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            result = (dfs(r+1, c, i+1)) or (dfs(r-1, c, i+1)) or (dfs(r, c+1, i+1)) or (dfs(r, c-1, i+1))
            path.remove((r, c))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

board = [["A","B","C","E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCES"
word = "ABCCED"
c = Solution()

print(c.exists(board, word))