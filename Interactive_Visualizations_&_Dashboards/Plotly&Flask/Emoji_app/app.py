from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/emoji.sqlite'

db = SQLAlchemy(app)

class Emoji(db.Model):
    __tablename__ = 'emoji'

    id = db.Column(db.Integer, primary_key=True)
    emoji_char = db.Column(db.String)
    emoji_id = db.Column(db.String)
    name = db.Column(db.String)
    score = db.Column(db.Integer)

    def __repr__(self):
        return '<Emoji %r>' % (self.name)

@app.before_first_request
def setup():
    #db.drop_all()
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emoji_char')
def emoji_char_data():
    results = db.session.query(Emoji.emoji_char,Emoji.score).order_by(Emoji.score.desc()).limit(10).all()

    emoji_char = [result[0] for result in results]
    scores = [int(result[1]) for result in results]

    plot_trace = {
        'x': emoji_char,
        'y': scores,
        'type':'bar'
    }
    return jsonify(plot_trace)

@app.route('/emoji_id')
def emoji_id_data():
    query_statement = db.session.query(Emoji).order_by(Emoji.score.desc()).limit(10).statement
    df = pd.read_sql_query(query_statement,db.session.bind)
    
    trace = {
        'x':df['emoji_id'].values.tolist(),
        'y':df['score'].values.tolist(),
        'type':'bar'
    }

    return jsonify(trace)

@app.route('/emoji_name')
def emoji_name_data():
    results = db.session.query(Emoji.name, Emoji.score).order_by(Emoji.score.desc()).limit(10).all()
    df = pd.DataFrame(results,columns=['name','score'])

    plot_trace = {
        'x':df['name'].values.tolist(),
        'y':df['score'].values.tolist(),
        'type':'bar'
    }

    return jsonify(plot_trace)

if __name__ == "__main__":
    app.run(port=4996,debug=True,use_reloader=True)
    
