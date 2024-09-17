from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    password = request.form['password']
    
    if username == "admin" and password == "secret":
        return f"Hello, {username}! You have successfully logged in."
    else:
        return "Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
