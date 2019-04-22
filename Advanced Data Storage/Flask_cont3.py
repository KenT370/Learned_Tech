from flask import Flask, jsonify

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

app = Flask(__name__)

@app.route('/')
def justice():
    return (f'Welcome to the API<br/>'
            f'Available Routes: <br/>'
            f'/api/v1.0/justice-league<br/>'
            f'Place the Name of the Superhero you want to see here: superhero/<superhero><br/>'
            f'Ex:  /api/v1.0/justice-league/superhero/batman<br/>'
            f'Or place the real name of the superhero you would like to see here: /real_name/<realname><br/>'
            f'Ex: /api/v1.0/justice-league/real_name/barryallen')

@app.route('/api/v1.0/justice-league/superhero/<superhero>')
def get(superhero): 
    for val in justice_league_members:
        if val['superhero'].replace(" ","").lower() == superhero.replace(" ","").lower():
            return jsonify(val)
    return jsonify({'error':f'SuperHero with name {superhero} not found. '}),404

@app.route('/api/v1.0/justice-league/real_name/<realname>')
def real_name(realname):
    for val in justice_league_members:
        if val['real_name'].replace(" ","").lower() == realname.replace(" ","").lower():
            return jsonify(val)
        return jsonify({'Error':'The name: {realname} not found.'}),404

if __name__ == "__main__":
    app.run(debug=True)