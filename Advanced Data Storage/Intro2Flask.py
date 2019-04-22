from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print('Something is Happening...!')
    return('Welcome to my first API')

@app.route("/about")
def about():
    print('Part 2')
    return('Name: Kenneth, Location: Sugarland')

@app.route("/contact")
def contact():
    print('Part 3')
    return('Email me @: Ragu@italian.com')

if __name__ == "__main__":
    app.run(debug=True)
