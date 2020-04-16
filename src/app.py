#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask, jsonify
from flask import request
from flask_pymongo import PyMongo
from flask.templating import render_template
from Models.Session import Session
from Models.UserSession import UserSession
from Services.Spark.sparkServices import produce_pi_service, split_words_service
app= Flask(__name__)
# connect to MongoDB with the defaults
#mongo1 = PyMongo(app, uri="mongodb://localhost:27017/off-top-db")
#@app.route(..) is a decorator. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#It takes a URL rule
app.config["MONGO_URI"] = "mongodb+srv://off-top-dev:offtop123@cluster0-ci5ku.gcp.mongodb.net/off-top-db"
app.config["JSON_SORT_KEYS"] = False
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/get-all-sessions', methods=['GET'])
def getAllSessions():
  session_collection = mongo.db.sessions.find({})
  sessions = []
  index = 0
  for session in session_collection:
    clean_session = {
      'id': index,
      "user_id":session["user_id"],
      "first_received_at": session["first_received_at"],
      "topic": session["topic"],
      "focus_score": session["focus_score"],
      "transcribed_at": session["transcribed_at"],
      "transcribed_speech": session["transcribed_speech"]
    }
    sessions.append(clean_session)
    index+=1
    all_sessions = {
      "sessions":sessions
    }
  return jsonify(all_sessions)
  

@app.route("/insert-session",methods=["POST"])      
def insertSession():
    # data = request.get_json()
    session_collection = mongo.db.sessions
    
    new_session = Session(
      request.form["user_id"],
      request.form["first_received_at"], 
      request.form["topic"], 
      request.form["focus_score"],
      request.form["transcribed_at"],
      request.form["transcribed_speech"]
    ).__dict__

    session_collection.insert_one(new_session)
    new_session['_id'] = str(new_session['_id'])
    return jsonify({'new_session' : new_session})

@app.route('/split-words', methods=["POST"])
def split_words():
  words = request.form.get("words")
  return split_words_service(words)

@app.route("/sparkpi", methods=["GET"])
def sparkpi():
    scale = int(request.args.get('scale', 2))
    pi = produce_pi_service(scale)
    response = "Pi is roughly {}".format(pi)
    return response

if __name__ == "__main__":
  app.run(debug=True)
