from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Home Page!")

@app.route('/login')
def login():
    return jsonify(message="Login Page")

@app.route('/dashboard')
def dashboard():
    return jsonify(message="Dashboard")

if __name__ == '__main__':
    app.run(host='124.0.0.0', port=8080, debug=True)
