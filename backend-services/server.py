#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask, jsonify, request
from flask.templating import render_template
from Models.UserSession import UserSession
from flask_restplus import Api
from datetime import datetime
from datetime import timedelta
from flask import session
from flask_cors import CORS, cross_origin
import requests
import json
from werkzeug.utils import cached_property # had error ImportError: cannot import name 'cached_property' from 'werkzeug' (C:\off-top-python\my-venv\lib\site-packages\werkzeug\__init__.py)
from Services.UserReportsService import user_reports_service # blueprint
from Services.UserSessionService import user_session_service # blueprint
from extensions import mongo, mysql

api = Api()
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://off-top-dev:offtop123@cluster0-ci5ku.gcp.mongodb.net/off-top-db"
app.config["JSON_SORT_KEYS"] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'offTop'

mysql.init_app(app)
mongo.init_app(app)
cors = CORS(app)


@app.route("/")
def hello():
    return "Hello World!"

app.register_blueprint(user_session_service)
app.register_blueprint(user_reports_service)    

api.init_app(user_session_service)
api.init_app(user_reports_service)

if __name__ == "__main__":
  app.run(debug=True)
