"""
This challenge was taken from an interview
"""

from dataclasses import dataclass


@dataclass
class Spacing:
    dots_padding: int
    dots_inner_space: int
    dots_outer_space: int

    dashs_padding: int
    dashs_inner_space: int
    dashs_outer_space: int


def calculate_spacings(row: int, prev_spacing: Spacing | None) -> Spacing:
    if row == 0:
        return Spacing(0, 3, 1, 1, 1, 3)
    if row == 1:
        return Spacing(2, 5, 5, 3, 3, 7)

    assert prev_spacing

    dots_padding = (prev_spacing.dots_padding * 2) + 1
    dots_inner_space = prev_spacing.dots_inner_space * 2 + 1
    dots_outer_space = prev_spacing.dots_outer_space * 2 + 1
    return Spacing(
        dots_padding,
        dots_inner_space,
        dots_outer_space,
        dots_padding + 1,
        dots_inner_space - 2,
        dots_outer_space + 2,
    )


def run(height: int):
    """
    Print a tree-like structure in the terminal given a height.
    Both the nodes and the edges should be printed.

    Example of a tree with a height of 5:
                           *                                 row = 4, padding = 23, inner space = 47, outer space = 47
       
                /                     \\                     row = 3, padding = 12, inner space = 21, outer space = 25
               *                       *                     row = 3, padding = 11, inner space = 23, outer space = 23
       
          /         \\            /         \\               row = 2, padding =  6, inner space =  9, outer space = 13
         *           *           *           *               row = 2, padding =  5, inner space = 11, outer space = 11
       
       /   \\      /   \\      /   \\       /   \\           row = 1, padding =  3, inner space =  3, outer space =  7
      *     *     *     *     *     *      *     *           row = 1, padding =  2, inner space =  5, outer space =  5

     / \\   / \\   / \\   / \\   / \\   / \\   / \\   / \\   row = 0, padding =  1, inner space =  1, outer space =  3
    *   *  *   *  *   *  *   *  *   *  *   *  *   *  *   *   row = 0, padding =  0, inner space =  3, outer space =  1
    """

    row = (height * 2) - 1
    grid = [[] for _ in range(row)]

    prev_spacing = None
    inverse_row = 0
    for row in range(row - 1, -2, -2):
        n_dots = 2 ** (row // 2)
        current_spacing = calculate_spacings(inverse_row, prev_spacing)
        prev_spacing = current_spacing

        # Pad row start
        grid[row].extend([" "] * current_spacing.dots_padding)

        if row == 0:
            # If it's the last row, add the dot and finish
            grid[row].append("*")
            break

        # Add dots
        for _ in range(n_dots // 2):
            grid[row].append("*")
            grid[row].extend([" "] * current_spacing.dots_inner_space)
            grid[row].append("*")
            grid[row].extend([" "] * current_spacing.dots_outer_space)

        # Add dashes
        grid[row - 1].extend([" "] * current_spacing.dashs_padding)
        for _ in range(n_dots // 2):
            grid[row - 1].append("/")
            grid[row - 1].extend([" "] * current_spacing.dashs_inner_space)

            grid[row - 1].append("\\")
            grid[row - 1].extend([" "] * current_spacing.dashs_outer_space)

        row -= 2
        inverse_row += 1

    return grid


def test_cases():
    return [
        (
            (2,),
            [[' ', ' ', '*'], [' ', '/', ' ', '\\', ' ', ' ', ' '], ['*', ' ', ' ', ' ', '*', ' ']],
        ),
        (
            (3,),
            [[' ', ' ', ' ', ' ', ' ', '*'], [' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' '], [' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' '], ['*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ']],
        ),
        (
            (5,),
            [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' '], [' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' '], ['*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ']],
        ),
    ]