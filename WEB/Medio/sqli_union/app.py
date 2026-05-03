from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Initialize database
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE users (id INTEGER, name TEXT, email TEXT)''')
c.execute('''INSERT INTO users VALUES (1, 'admin', 'admin@example.com')''')
c.execute('''CREATE TABLE flags (id INTEGER, flag TEXT)''')
c.execute('''INSERT INTO flags VALUES (1, 'CTF{sqli_union_flag}')''')
conn.commit()

@app.route('/search')
def search():
    user = request.args.get('user', '')
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE name = '{user}'"
    try:
        c.execute(query)
        result = c.fetchall()
        return f"<h1>Results: {result}</h1>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
