''' Flask app that connects to scrape_costa.py that scrapes data from 
two different websites and pulls the data into a MongoDB.  The Flask
App then pulls the data from the MongoDB and pushes it to the index.html
to display the data on a webpage 
'''



import scrape_costa
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import ReplaceOne
import pymongo

# First Database Connection
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/temp_dict'
mongo = PyMongo(app)

# 2nd Database Connection
mongo2 = PyMongo(app,uri='mongodb://localhost:27017/craig_dict')

@app.route('/')
def home():
    temp_dict = mongo.db.temp_dict.find_one()
    craig_db = mongo2.db.craig.find()
    return render_template('index.html',dict=temp_dict,
                            craig_dict = craig_db)

@app.route('/scrape')
def scrape():
    temp_dict = mongo.db.temp_dict
    dict_data, craig_db = scrape_costa.scrape_info()
    temp_dict.update({}, dict_data,upsert=True)

    # 2nd Database Connection
    mongo2.db.craig.bulk_write([
    ReplaceOne(
        { "title": m['title']},
         m,
         upsert=True
         )
         for m in craig_db
         ])
    
    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)
