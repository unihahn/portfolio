from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('cafe.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/menu', methods=['GET'])
def get_menu():
    conn = get_db_connection()
    menu_items = conn.execute('SELECT * FROM menu_items').fetchall()
    conn.close()
    return jsonify([dict(row) for row in menu_items])

@app.route('/api/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO menu_items (name, price, description, category) VALUES (?, ?, ?, ?)',
                   (data['name'], data['price'], data.get('description'), data['category']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Menu item added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
