from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/menu', methods=['GET'])
def get_menu():
    # Replace this with your actual menu data
    menu = [
        {'id': 1, 'name': 'Coffee', 'price': 2.50},
        {'id': 2, 'name': 'Tea', 'price': 2.00},
        {'id': 3, 'name': 'Sandwich', 'price': 5.00}
    ]
    return jsonify(menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)

