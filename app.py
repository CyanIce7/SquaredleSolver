from flask import Flask, render_template, request, jsonify
from solver import SquaredleGraph, generate_trie, find_word

app = Flask(__name__)

SQUAREDLE_GRID = [["t", "a", "v", "n"],
                  ["n", "d", "r", "i"],
                  ["g", "a", "i", "i"],
                  ["m", "u", "qu", "m"]]

grid_size = len(SQUAREDLE_GRID)

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
    is_valid_word = False
    is_repeat = False

    # Check if the word has been found already
    if word in stored_words:
        is_valid_word = True
        is_repeat = True
    # Store the word if it is longer than 1 letter and not a duplicate
    elif len(word) > 1 and find_word(word, trie):
        stored_words.append(word)
        is_valid_word = True

    # Reset all cells to inactive
    for r in range(grid_size):
        for c in range(grid_size):
            server_grid[r][c]['active'] = 0

    # Send the updated list of words back to JavaScript
    return jsonify({'status': 'success', 'words': stored_words, 'valid': is_valid_word, 'repeat': is_repeat})

@app.route('/reset_words', methods=['POST'])
def reset_words():
    stored_words.clear() # Empties the Python list
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    squaredle_graph = SquaredleGraph(SQUAREDLE_GRID)
    trie = generate_trie()
    app.run(debug=True)
