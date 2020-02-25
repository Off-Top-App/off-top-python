#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask,jsonify
from flask_pymongo import PyMongo
from  flask import render_template

app= Flask(__name__)
# connect to MongoDB with the defaults
#mongo1 = PyMongo(app, uri="mongodb://localhost:27017/off-top-db")
#@app.route(..) is a decorator. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#It takes a URL rule
app.config["MONGO_URI"] = "mongodb+srv://off-top-dev:offtop123@cluster0-ci5ku.gcp.mongodb.net/off-top-db"
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/sessions")      
def home_page():
    sessions = mongo.db.sessions
    output = []
    for session in sessions.find():
        print(session)
        output.append({'_id': str(session['_id']), 'words': session['words']})

    return jsonify({'sessions' : output})
if __name__ == "__main__":
  app.run(debug=True)
