from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage for quotes
quotes = []

# GET endpoint to retrieve all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes), 200

# POST endpoint to add a new quote
@app.route('/quotes', methods=['POST'])
def add_quote():
    new_quote = request.json
    quotes.append(new_quote)
    return jsonify(new_quote), 201

# PUT endpoint to update an existing quote
@app.route('/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    if quote_id < len(quotes):
        quotes[quote_id] = request.json
        return jsonify(quotes[quote_id]), 200
    return jsonify({'error': 'Quote not found'}), 404

# DELETE endpoint to remove a quote
@app.route('/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    if quote_id < len(quotes):
        deleted_quote = quotes.pop(quote_id)
        return jsonify(deleted_quote), 200
    return jsonify({'error': 'Quote not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)