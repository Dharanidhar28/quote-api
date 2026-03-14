import sqlite3

from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

# Sample database storage for quotes
DATABASE = "quotes.db"



# Create database and table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')




# GET endpoint to retrieve all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quotes")
    rows = cursor.fetchall()

    quotes = []
    for row in rows:
        quotes.append({"id": row[0], "quote": row[1]})

    conn.close()

    return jsonify(quotes)

# POST endpoint to add a new quote
@app.route('/quotes', methods=['POST'])
def add_quote():
    new_quote = request.json
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quotes (quote) VALUES (?)", (new_quote['quote'],))
    conn.commit()
    conn.close()
    return jsonify({"quote": new_quote['quote']}), 201

# PUT endpoint to update an existing quote
@app.route('/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE quotes SET quote = ? WHERE id = ?", (request.json['quote'], quote_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Quote updated'}), 200

# DELETE endpoint to remove a quote
@app.route('/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quotes WHERE id = ?", (quote_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Quote deleted'}), 200

import random

@app.route('/generate-quote', methods=['GET'])
def generate_quote():

    ai_quotes = [
        "Success is built from small daily efforts.",
        "Discipline today creates freedom tomorrow.",
        "Your future is created by what you do today.",
        "Small progress every day leads to big results.",
        "Consistency beats motivation."
    ]

    quote = random.choice(ai_quotes)

    return jsonify({
        "quote": quote
    })

if __name__ == '__main__':
    init_db()
    print("\nAPI ROUTES\n")

    for rule in app.url_map.iter_rules():
        print(f"{rule.methods}  {rule}")
    
    app.run(debug=True)