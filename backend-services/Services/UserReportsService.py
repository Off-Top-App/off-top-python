from flask import Blueprint
from flask import json
import requests
from flask import session, request, jsonify
from Services.UserSessionService import getAllSessions
from datetime import datetime
from extensions import mysql
# userreports.py <-- userSessionDuration()

user_reports_service = Blueprint("user_reports", __name__)


@user_reports_service.route("/get-user-session-duration")
def userSessionDuration():
        sessions = getAllSessions()
        all_sessions = sessions.json.get("sessions")
        user_ids = [1, 2, 3, 4, 5, 6]
        user_time_list = []
        user_sesssion_duration_list = []

        for user_id in user_ids:
            user_transcribed_counter = 0
            transcribed_list = []
            for session in all_sessions:
                session_user_id = int(session['user_id'])
                if user_id == session_user_id:
                    time = datetime.strptime(
                    session["transcribed_at"], '%Y-%m-%d %H:%M:%S.%f')
                    transcribed_list.append(str(time))
                    user_transcribed_counter += 1
        user_time={
        "user_id": user_id,
        "first_transcribed_at": 0,
        "last_transcribed_at": user_transcribed_counter,
        "transcribed_list": sorted(transcribed_list)
        }
        user_time_list.append(user_time)

        return jsonify(user_sesssion_duration_list)

@user_reports_service.route("/get-user-topic", methods=["GET"])
def aggregateUserTopics():
    sessions = getAllSessions()
    all_sessions = sessions.json.get("sessions")
    user_ids = [1,2,3,4,5,6]
    user_topic_list = []

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

@user_reports_service.route('/get-users-avg-scores', methods=['GET'])
def userAverageFocusScore():
  sessions = getAllSessions()
  all_sessions = sessions.json.get("sessions")

  user_ids = [1,2,3,4,5,6]
  user_score_list =[]
  summedScore = 0
  user_session_count = 0

  for user_id in user_ids:
    for session in all_sessions:
      session_user_id = int(session['user_id'])
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

@user_reports_service.route('/get-users-profession-with-score', methods=['GET'])
def getProfession():
  users = retrieveUser()
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
               "avg_focus_score": score ["avg_focus_score"],
               "profession" : user["professional"]
             }
             profession_list.append(profession_object)
             profession_with_score ={
               "profession_with_score":profession_list
             }
  return jsonify(profession_with_score)

@user_reports_service.route('/get-user-information', methods=['GET'])
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

@user_reports_service.route('/merge-user-data',methods=['GET']) 
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
