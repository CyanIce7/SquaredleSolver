"""
Flask test
"""
from flask import Flask, render_template, request
import solver
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        grid_text = request.form.get('grid')
        if not check_valid_grid(grid_text):
            return f"Invalid grid. Try again!"
        grid = grid_text_to_list(grid_text)
        return f"{grid}"

    return render_template('index.html')

def check_valid_grid(grid_text: str) -> bool:
    """
    Checks whether the inputted grid text corresponds to a valid grid.

    Criteria:
        - All rows must have the same length
        - All characters must either be an alphabetical character, -, or /
    >>> check_valid_grid("abcdfeg")
    True
    >>> check_valid_grid("AbFGUEGHJEf")
    True
    >>> check_valid_grid("cbd/efg")
    True
    >>> check_valid_grid("hjdkgr/hu")
    False
    >>> check_valid_grid("--hh--/boo--p")
    True
    >>> check_valid_grid("////")
    False
    >>> check_valid_grid("abcd/gehf/gh-y/hh7t")
    False
    """
    # Check whether input is a rectangle
    row_lengths = {len(i) for i in grid_text.split("/")}
    if len(row_lengths) != 1 or 0 in row_lengths:
        return False

    # Check whether valid characters are inputted
    for c in grid_text:
        if not (c.isalpha() or c == "/" or c == "-"):
            return False

    return True

def grid_text_to_list(grid_text: str) -> list[list[str]]:
    grid = [[]]
    curr_row = 0
    for char in grid_text:
        if char == "-":
            grid[curr_row].append("-")
        elif char == "/":
            grid.append([])
            curr_row += 1
        else:
            grid[curr_row].append(char.lower())
    return grid


if __name__ == '__main__':
    app.run(debug=True)

