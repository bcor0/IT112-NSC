from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'db.sqlite'

# Helper function
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create table
def create_table():
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT
            )
        ''')

create_table()

# Get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    db = get_db()
    items = db.execute('SELECT * FROM items').fetchall()
    db.close()
    return jsonify([dict(row) for row in items]), 200

# Add new item
@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    try:
        db = get_db()
        db.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
        db.commit()
        db.close()
        return jsonify({'message': 'Inserted!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
