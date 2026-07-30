# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return "Hello, student good morning!"
# app.run(debug=True)

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello, Student Good Morning!"
# @app.route('/about')
# def about():
#     return "This is a simple Flask application."
# app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/about")
def about():
    return "Welcome to About Page"

@app.route("/contact")
def contact():
    return "Welcome to Contact Page"

if __name__ == "__main__":
    app.run(debug=True)