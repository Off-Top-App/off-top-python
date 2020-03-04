#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask, jsonify
from flask import request
from flask_pymongo import PyMongo
from flask.templating import render_template
from Models.session import Session
from Services.Spark.sparkServices import produce_pi_service, split_words_service
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

@app.route("/sessions",methods=["POST"])      
def sessions():
    data = request.get_json()
    session_collection = mongo.db.sessions
    
    new_session = Session( data["user_id"],data["first_received_at"],data["focus_score"],data["transcribed_at"],data["transcribed_speech"])
    print(new_session.__dict__)
    session_collection.insert(new_session.__dict__)
    # session_collection.insert({
    #     "user_id":data["user_id"],
    #     "first_received_at": data["first_received_at"],
    #     "focus_score": data["focus_score"],
    #     "transcribed_at": data["transcribed_at"],
    #     "transcribed_speech": data["transcribed_speech"]
    # })
    output = []
    for session in session_collection.find():
        print(session)
        output.append({
            '_id': str(session['_id']),
            "user_id":session["user_id"],
            "first_received_at": session["first_received_at"],
            "focus_score": session["focus_score"],
            "transcribed_at": session["transcribed_at"],
            "transcribed_speech": session["transcribed_speech"]
        })

    return jsonify({'sessions' : output})

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
