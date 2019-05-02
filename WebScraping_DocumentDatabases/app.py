import scrape_costa
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/temp_dict'
mongo = PyMongo(app)


@app.route('/')
def home():
    temp_dict = mongo.db.temp_dict.find_one()
    
    return render_template('index.html',dict=temp_dict)

@app.route('/scrape')
def scrape():
    temp_dict = mongo.db.temp_dict

    dict_data = scrape_costa.scrape_info()

    temp_dict.update({}, dict_data,upsert=True)

    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)
