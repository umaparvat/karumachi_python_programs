"""
Brute force solution
youtube link : https://www.youtube.com/watch?v=Ph95IHmRp5M
leetcode : https://leetcode.com/problems/n-queens/
O(n!)
"""


class Solution:

    def __init__(self):
        self.column = set()
        self.positive_diagonal = set()
        self.negative_diagonal = set()
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtrack(0, n, board)
        return self.result

    def backtrack(self, row, n, board):
        if row == n:
            board_copy = ["".join(i) for i in board]
            self.result.append(board_copy)
            return

        for column_index in range(n):
            if column_index in self.column or (row + column_index) in self.positive_diagonal or (
                    row - column_index) in self.negative_diagonal:
                continue
            self.column.add(column_index)
            self.positive_diagonal.add(row + column_index)
            self.negative_diagonal.add(row - column_index)
            board[row][column_index] = "Q"

            self.backtrack(row + 1, n, board)

            self.column.remove(column_index)
            self.positive_diagonal.remove(row + column_index)
            self.negative_diagonal.remove(row - column_index)
            board[row][column_index] = "."
