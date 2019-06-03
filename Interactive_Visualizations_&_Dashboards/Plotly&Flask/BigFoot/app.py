# Pulling Data from a SQLite Database and Using Javascript
# to extract the data from self created '/data' API to 
# render a Plot in the 'index.html' file

import pandas as pd
from sqlalchemy import Table, Column, Integer, String
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/bigfoot.sqlite'
db = SQLAlchemy(app)

class bigfoot(db.Model):
    __tablename__ = 'bigfoot'
    
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer)
    title = db.Column(db.String)
    classification = db.Column(db.String)
    timestamp = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    
    def __repr__(self):
        return '<BigFoot %r>' % (self.name)
    
@app.before_first_request
def setup():
    #db.drop_all()
    db.create_all()




@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/data')
def data():
    sel = [func.strftime('%Y',bigfoot.timestamp),func.count(bigfoot.id)]
    results = db.session.query(*sel).group_by(func.strftime('%Y',bigfoot.timestamp)).all()

    results_df = pd.DataFrame(results,columns=['Year','Count'])

    results_dictionary = {
        'x':results_df['Year'].tolist(),
        'y':results_df['Count'].tolist(),
        'type':'scatter',
        'name': 'BigFoot Sightings'
    }
    return jsonify(results_dictionary)

if __name__ == '__main__':
    app.run(debug=True)