#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from flask.templating import render_template
from Services.Spark.sparkServices import produce_pi_service, split_words_service

app= Flask(__name__)
# connect to MongoDB with the defaults
# mongo1 = PyMongo(app, uri="mongodb://localhost:27017/off-top-db")
#@app.route(..) is a decorator. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#It takes a URL rule
app.config['MONGO_DBNAME'] = 'off-top-db' # name of database on mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/off-top-db"
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"
# def home_page():
    # online_users= mongo1.db.users.find({"online": True})
    # return render_template("index.html", online_users= online_users)
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
