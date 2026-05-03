from flask import Flask, request
import pickle
import base64

app = Flask(__name__)

@app.route('/load')
def load():
    try:
        data = base64.b64decode(request.args.get('data', ''))
        result = pickle.loads(data)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
