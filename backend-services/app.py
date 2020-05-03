#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask, jsonify
from flask import request
from flask_pymongo import PyMongo
from flask.templating import render_template
from Models.UserSession import UserSession
from flask import session
from flask_mysqldb import MySQL
import requests
import json

app= Flask(__name__)
# connect to MongoDB with the defaults
#@app.route(..) is a decorator. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#It takes a URL rule
app.config["MONGO_URI"] = "mongodb+srv://off-top-dev:offtop123@cluster0-ci5ku.gcp.mongodb.net/off-top-db"
app.config["JSON_SORT_KEYS"] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'offTop'

mysql = MySQL(app)
mongo = PyMongo(app)

@app.route('/get-user-topic', methods=['GET'])
def aggregateUserTopics():
  sessions = getAllSessions()
  all_sessions = sessions.json.get("sessions")

  user_ids = [1,2,3,4,5,6]
  user_topic_list =[]
  
  for user_id in user_ids:
    for session in all_sessions:
      session_user_id = int(session['user_id'])
      if user_id == session_user_id:
        user_topic={
          "user_id": session_user_id,
          "topic": session["topic"]
        }
        if user_topic not in user_topic_list:
          user_topic_list.append(user_topic)

  return jsonify(user_topic_list)

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

@app.route('/get-user-information', methods=['GET'])
def retrieveUser():
      cur = mysql.connection.cursor()
      cur.execute ("SELECT * FROM user")
      fetchdata = cur.fetchall()
      cur.close()
       
      users = []
    
      for row in fetchdata:
          user_info = {
              "user_id":row[0],
              "age":row[1],
              "city":row[2],
              "first_name":row[6],
              "last_name":row[8],
              "email":row[5],
              "gender":row[7],
              "user_name":row[11],
              "password":row[9],
              "professional":row[10],
              "created_at":row[3],
              "deleted_at":row[4]
              }
          users.append(user_info)
          all_users = {
          "Users":users
          }
     
      return jsonify(all_users)

@app.route('/merge-user-data',methods=['GET'])
def mergeUserData(): 
  users = retrieveUser()
  get_users = users.json.get("Users")
  sessions = getAllSessions()
  all_sessions = sessions.json.get("sessions")
  user_info_session_list = []

  for user in get_users:
        user_list = {
             "user_id": user["user_id"],
             "first_name": user["first_name"],
             "last_name": user["last_name"],
             "gender": user["gender"],
             "profession": user["professional"],
                 }

        user_id = int(user["user_id"])
        session_list = []
        for session in all_sessions:
            session_user_id = int(session["user_id"])
            if user_id == session_user_id:

             session_object = {
              "first_received_at": session["first_received_at"],
               "topic": session["topic"],
               "focus_score": session["focus_score"],
               "transcribed_at": session["transcribed_at"],
               "transcribed_speech": session["transcribed_speech"]
                      }
            session_list.append(session_object)
            user_list["session"] = session_list

            if user_id not in user_info_session_list:
                  user_info_session_list.append(user_list)

  return jsonify(user_info_session_list)
              

if __name__ == "__main__":
  app.run(debug=True)
