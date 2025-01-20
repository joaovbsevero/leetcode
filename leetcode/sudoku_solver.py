"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

-----------------------------------------

Example 1:

    Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:
* board.length == 9
* board[i].length == 9
* board[i][j] is a digit or '.'.
* It is guaranteed that the input board has only one solution.

-----------------------------------------

Reference: https://leetcode.com/problems/sudoku-solver
"""


def run(board: list[list[str]]) -> list[list[str]]:
    def filter_possible_values(
        row: int,
        column: int,
    ) -> list[str]:
        """
        Find all possible values for the given row and column.

        Possible values are the ones that satisfy the condition given by the rules of Sudoku.

        The rules are:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        :param row: The row index.
        :param column: The column index.
        :return: A list of possible values.
        """

        possible_values_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        possible_values_set.difference_update(set(board[row]))
        if not possible_values_set:
            return []

        possible_values_set.difference_update({board[i][column] for i in range(9)})
        if not possible_values_set:
            return []

        start_row = row - (row % 3)
        start_column = column - (column % 3)

        possible_values_set.difference_update(
            {
                board[start_row + row_idx][start_column + column_idx]
                for row_idx in range(3)
                for column_idx in range(3)
            }
        )

        return list(possible_values_set)

    def solve_board(start_row: int, start_column: int) -> bool:
        """
        Solve the board using backtracking.

        Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution
        incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the
        problem at any point of time (by time, here, is referred to the number of steps involved in reaching the
        solution).

        :param start_row: The row index to start from.
        :param start_column: The column index to start from.
        :return: True if the board is solved, False otherwise.
        """

        for row_idx in range(start_row, len(board)):
            for column_idx in range(start_column, len(board[row_idx])):
                value = board[row_idx][column_idx]
                if value != ".":
                    continue

                possible_values = filter_possible_values(row_idx, column_idx)
                for possible_value in possible_values:
                    board[row_idx][column_idx] = possible_value
                    solved = solve_board(
                        start_row=row_idx,
                        start_column=column_idx + 1,
                    )
                    if solved:
                        return True

                board[row_idx][column_idx] = "."
                return False

            start_column = 0

        return True

    solve_board(0, 0)
    return board


def test_cases():
    return [
        (
            (
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ],
            ),
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
        ),
        (
            (
                [
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", "9", ".", ".", "1", ".", ".", "3", "."],
                    [".", ".", "6", ".", "2", ".", "7", ".", "."],
                    [".", ".", ".", "3", ".", "4", ".", ".", "."],
                    ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", "2", "5", ".", "6", "4", ".", "."],
                    [".", "8", ".", ".", ".", ".", ".", "1", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ],
            ),
            [
                ["7", "2", "1", "8", "5", "3", "9", "4", "6"],
                ["4", "9", "5", "6", "1", "7", "8", "3", "2"],
                ["8", "3", "6", "4", "2", "9", "7", "5", "1"],
                ["9", "6", "7", "3", "8", "4", "1", "2", "5"],
                ["2", "1", "4", "7", "6", "5", "3", "9", "8"],
                ["3", "5", "8", "2", "9", "1", "6", "7", "4"],
                ["1", "7", "2", "5", "3", "6", "4", "8", "9"],
                ["6", "8", "3", "9", "4", "2", "5", "1", "7"],
                ["5", "4", "9", "1", "7", "8", "2", "6", "3"],
            ],
        ),
    ]
