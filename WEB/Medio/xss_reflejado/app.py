from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    # Vulnerable to XSS
    return f"<h1>{q}</h1>"

@app.route('/')
def index():
    return '''
    <html>
    <head><title>Search</title></head>
    <body>
    <h1>Search Tool</h1>
    <form action="/search" method="GET">
        <input type="text" name="q" placeholder="Search...">
        <input type="submit" value="Search">
    </form>
    <p>Hint: The flag is in a script comment. Can you extract it using XSS?</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=3000)
