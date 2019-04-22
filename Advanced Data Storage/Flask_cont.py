from flask import Flask, jsonify

justice = [
    {"superhero":"Aquaman","real_name":"Arthur Curry"},
    {"superhero": 'Batman',"real_name": "Bruce Wayne"},
    {"superhero": "Cyborg","real_name": "Victor Stone"},
    {"superhero": "Flash","real_name":"Barry Allen"},
    {"superhero": "Green Lantern","real_name":"Hal Jordan"},
    {"superhero": "Superman","real_name":"Clark Kent"},
    {"superhero": "Wonder Woman","real_name":"Princess Diana"},
]
app = Flask(__name__)

@app.route('/')
def first():
    print('Its valuable!!')
    return("Welcome to the Justice League API!\nAvailable Routes:\n/api/v1.-/justice-league")

@app.route("/api/v1.0/justice-league")
def GET():
    return jsonify(justice)

if __name__=='__main__':
    app.run(debug=True)