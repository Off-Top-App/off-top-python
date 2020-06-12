from flask import Blueprint, jsonify
from extensions import mongo


user_session_service = Blueprint("user_session", __name__)


@user_session_service .route("/get-all-sessions", methods=["GET"])
def getAllSessions():
    session_collection = mongo.db.sessions.find({})
    sessions = []
    index = 0
    for session in session_collection:
        clean_session = {
          'id': index,
          "user_id": session["user_id"],
          "first_received_at": session["first_received_at"],
          "topic": session["topic"],
          "focus_score": session["focus_score"],
          "transcribed_at": session["transcribed_at"],
          "transcribed_speech": session["transcribed_speech"]
        }
        sessions.append(clean_session)
        index += 1
        all_sessions = {
          "sessions": sessions
        }
    return jsonify(all_sessions)


@user_session_service .route("/insert-session", methods=["POST"])
def insertSession():
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
