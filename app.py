from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

grid_size = 3

SQUAREDLE_GRID = [["U", "T", "S"],
                  ["D", "H", "E"],
                  ["R", "O", "N"]]

# Create a 4x4 grid where each cell holds a random uppercase letter
server_grid = [
    [{'letter': SQUAREDLE_GRID[i][j], 'active': 0} for j in range(grid_size)]
    for i in range(grid_size)
]


@app.route('/')
def index():
    return render_template('grid.html', grid=server_grid, size=grid_size)


@app.route('/activate_cell', methods=['POST'])
def activate_cell():
    data = request.get_json()
    row = int(data['row'])
    col = int(data['col'])

    # Set the cell to active
    server_grid[row][col]['active'] = 1
    return jsonify({'status': 'success'})


@app.route('/clear_grid', methods=['POST'])
def clear_grid():
    # Reset all cells to inactive
    for r in range(grid_size):
        for c in range(grid_size):
            server_grid[r][c]['active'] = 0

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
