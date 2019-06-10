from flask import Flask, render_template,jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
#from flask.ext.heroku import heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zphvqfcqbejonu:86c66f04c54f05d6fc6ad5adc2683dcb2e3d9bfbbc4c01c42d0005c70ee66807@ec2-54-83-201-84.compute-1.amazonaws.com:5432/d8hgnkhff30apd'
db = SQLAlchemy(app)
    
from .models import Pet

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        name = request.form['petname']
        lat = request.form['Latitude']
        lon = request.form['Longitude']
        
        pet = Pet(name=name,lat=lat,lon=lon)
        db.session.add(pet)
        db.session.commit()

        return redirect('/',code=302)

    return render_template('form.html')

@app.route('/api/pals')
def data():
    results = db.session.query(Pet).all()
    name = [var.name for var in results]
    lat = [var.lat for var in results]
    lon = [var.lon for var in results]

    dic = {
        'type':'scattergeo',
        'mode':'markers+text',
        'text':name,
        'lon':lon,
        'lat':lat,
        'marker':{'size':10},
        'name': 'Pet Locations',
        'textposition': 'top center'
    }

    return jsonify(dic)

if __name__ == '__main__':
    app.run()

# class Pet(db.Model):
#     __tablename__ = 'pets'

#     id = db.Column(db.*)
#     lat = db.Column(db.Float)
#     lon = db.Column(db.Float)

#     def __repr__(self):
#         return '<Pet %r>' % (self.name)
        