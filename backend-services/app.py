#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask, jsonify
from flask import request
from flask_pymongo import PyMongo
from flask.templating import render_template
from Models.UserSession import UserSession
from datetime import datetime
from datetime import timedelta
from flask import session
from flask_mysqldb import MySQL
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np


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

@app.route("/get-user-session-duration")
def userSessionDuration():
  sessions = getAllSessions()
  all_sessions = sessions.json.get("sessions")

  users = retrieveUsers().json.get("Users")
  user_time_list = []
  user_sesssion_duration_list = []

  for user in users:
    user_id = int(user['user_id'])
    user_transcribed_counter = 0
    transcribed_list = []
    for session in all_sessions:
      session_user_id = int(session['user_id'])
      if user_id == session_user_id:
        time = datetime.strptime(session["transcribed_at"], '%Y-%m-%d %H:%M:%S.%f')
        transcribed_list.append(str(time))
        user_transcribed_counter += 1

    user_time ={
      "user_id": user_id,
      "first_transcribed_at": 0,
      "last_transcribed_at": user_transcribed_counter,
      "transcribed_list": sorted(transcribed_list)
    }
    user_time_list.append(user_time)
    
  for user in user_time_list:
    first = user["first_transcribed_at"]
    last = user["last_transcribed_at"]
    transcribed_arr = user["transcribed_list"]
    
    last_time = datetime.strptime(transcribed_arr[last - 1], '%Y-%m-%d %H:%M:%S.%f')
    first_time = datetime.strptime(transcribed_arr[first], '%Y-%m-%d %H:%M:%S.%f')
    
    t1 = timedelta(hours=first_time.hour, minutes=first_time.minute, seconds=first_time.second)
    t2 = timedelta(hours=last_time.hour, minutes=last_time.minute, seconds=last_time.second)
    
    duration = t2 - t1
    user_sesssion_duration = {
      "user_id": user["user_id"],
      "session_duration": str(duration)
    }
    user_sesssion_duration_list.append(user_sesssion_duration)

  return jsonify(user_sesssion_duration_list)

@app.route('/get-user-topic', methods=['GET'])
def aggregateUserTopics():
  sessions = getAllSessions()
  all_sessions = sessions.json.get("sessions")

  users = retrieveUsers().json.get("Users")
  user_topic_list =[]

  for user in users:
    user_id = user['user_id']
    for session in all_sessions:
      session_user_id = int(session['user_id'])
      if user_id == session_user_id:
        user_topic={
          "user_id": session_user_id,
          "topic": session["topic"]
        }
      if user_topic not in user_topic_list:
        user_topic_list.append(user_topic)
  visualizeTopics()
  return jsonify(user_topic_list)

def visualizeTopics():
  outputFile = "topicChart.png"
  plt.switch_backend('Agg')
  sizes= [33.3, 33.3, 33.3]
  labels= ['sports', 'food', 'computer science']
  colors = ['gold', 'yellowgreen', 'lightcoral']
  explode = (0, 0, 0)  # explode 1st slice

  plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=140)
  plt.title("Topics")
  plt.axis('equal')
  plt.savefig(outputFile)
  plt.show()

@app.route('/get-users-avg-scores', methods=['GET'])
def userAverageFocusScore():
  sessions = getAllSessions()
  all_sessions = sessions.json.get("sessions")

  user_ids = retrieveUsers().json.get("Users")
  user_score_list =[]
  summedScore = 0
  user_session_count = 0

  for user in user_ids:
    for session in all_sessions:
      session_user_id = int(session['user_id'])
      user_id = int(user['user_id'])
      if user_id == session_user_id:
        user_session_count +=1
        if session['focus_score'] == 'true':
          summedScore += 1

    avgScore = 10*(summedScore/user_session_count)

    summedScore = 0
    user_session_count = 0
    user_avgScore = {
      "user_id": user_id,
      "avg_focus_score": avgScore
    }
    user_score_list.append(user_avgScore)

    if user_avgScore not in user_score_list:
      user_score_list.append(user_avgScore)

    user_score_lists={
      "avgScore":user_score_list
    }

  return jsonify(user_score_lists)

@app.route('/get-users-profession-with-score', methods=['GET'])
def getProfession():
  users = retrieveUsers()
  get_users = users.json.get("Users")
  user_average_score = userAverageFocusScore()
  scores = user_average_score.json.get("avgScore")
  profession_list = []

  for user in get_users:
     for score in scores: 
       user_id = int (user["user_id"])
       score_from_userAverageFocusScore = int (score["user_id"])

       if user_id == score_from_userAverageFocusScore:
             profession_object ={
               "user_id": score["user_id"],
               "avg_focus_score": score["avg_focus_score"],
               "profession" : user["professional"]
             }
             profession_list.append(profession_object)
             profession_with_score ={
               "profession_with_score":profession_list
             }
  visualizeFocus(profession_with_score)
  return jsonify(profession_with_score)

def visualizeFocus(users):
  professions = []
  focus_scores = []
  colors = []
  for user in users['profession_with_score']:
    professions.append(user['profession'])
    focus_scores.append(user['avg_focus_score'])
    print(int(user['avg_focus_score']))
    if(int(user['avg_focus_score']) >= 7.0):
      colors.append('green')
    elif(int(user['avg_focus_score']) > 4.0 and int(user['avg_focus_score']) < 7.0):
      colors.append('yellow')
    else:
      colors.append('red')

  plt.switch_backend('Agg')
  legend_elements = [
    Line2D([0], [0], color='g', lw=4, label='Good Focus Score'),
    Line2D([0], [0], color='y', lw=4, label='Decent Focus Score'),
    Line2D([0], [0], color='r', lw=4, label='Bad Focus Score'),
  ]
  plt.legend(handles=legend_elements)



  outputFile = "focus_scores.png"
  index = np.arange(len(professions))
  plt.bar(index, focus_scores, color=colors, edgecolor='black')
  plt.xlabel('User Professions', fontsize=10)
  plt.ylabel('Focus Scores', fontsize=12)
  plt.xticks(index, professions, fontsize=8, rotation=0)
  plt.title('User Focus Scores')
  plt.savefig(outputFile)
  plt.show()

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
def retrieveUsers():
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
  users = retrieveUsers()
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
