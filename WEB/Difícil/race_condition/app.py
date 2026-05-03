from flask import Flask
from time import sleep
import threading

app = Flask(__name__)

# Global state
balance = 100
lock = threading.Lock()

@app.route('/balance')
def get_balance():
    return f"Balance: {balance}"

@app.post('/buy')
def buy():
    global balance
    # Vulnerable to race condition
    if balance >= 10:
        sleep(1)  # Simulate processing
        balance -= 10
        return "OK"
    return "FAIL"

@app.route('/flag')
def flag():
    if balance <= 0:
        return "CTF{race_cond_won}"
    return "Keep buying..."

if __name__ == '__main__':
    app.run(debug=True, port=3000, threaded=True)
