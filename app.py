from flask import Flask, render_template, request, jsonify
from solver import SquaredleGraph, generate_trie, find_word

app = Flask(__name__)

grid_size = 3

SQUAREDLE_GRID = [["u", "t", "s"],
                  ["d", "h", "e"],
                  ["r", "o", "n"]]

server_grid = [
    [{'letter': SQUAREDLE_GRID[i][j], 'active': 0} for j in range(grid_size)]
    for i in range(grid_size)
]

stored_words = []

@app.route('/')
def index():
    return render_template('index.html', grid=server_grid, size=grid_size)


@app.route('/activate_cell', methods=['POST'])
def activate_cell():
    data = request.get_json()
    row = int(data['row'])
    col = int(data['col'])

    # Set the cell to active
    server_grid[row][col]['active'] = 1
    return jsonify({'status': 'success'})


@app.route('/deactivate_cell', methods=['POST'])
def deactivate_cell():
    data = request.get_json()
    row = int(data['row'])
    col = int(data['col'])

    # Set the cell back to inactive
    server_grid[row][col]['active'] = 0
    return jsonify({'status': 'success'})


@app.route('/clear_grid', methods=['POST'])
def clear_grid():
    # Reset all cells to inactive
    for r in range(grid_size):
        for c in range(grid_size):
            server_grid[r][c]['active'] = 0

    return jsonify({'status': 'success'})


@app.route('/submit_word', methods=['POST'])
def submit_word():
    data = request.get_json()
    word = data.get('word', '').strip()
    print(word)

    # Store the word if it is longer than 1 letter and not a duplicate
    if len(word) > 1 and word not in stored_words and find_word(word, trie):
        stored_words.append(word)

    # Reset all cells to inactive
    for r in range(grid_size):
        for c in range(grid_size):
            server_grid[r][c]['active'] = 0

    # Send the updated list of words back to JavaScript
    return jsonify({'status': 'success', 'words': stored_words})


if __name__ == '__main__':
    squaredle_graph = SquaredleGraph(SQUAREDLE_GRID)
    trie = generate_trie()
    app.run(debug=True)
