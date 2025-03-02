from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = {
    '001': {
        'ID': '001',
        'TITLE': 'MARVEL SPIDERMAN',
        'AUTHOR': 'STAN LEE',
        'PUBLICATION_DATE': '2002-08-01'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not all(key in data for key in ['ID', 'TITLE', 'AUTHOR', 'PUBLICATION_DATE']):
        return jsonify({'message': 'All fields are required'}), 400
    
    book_id = data['ID']
    books[book_id] = data
    return jsonify({'message': 'Book added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
