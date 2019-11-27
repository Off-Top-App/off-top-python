#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask
from flask_pymongo import PyMongo

app= Flask(__name__)
# connect to MongoDB with the defaults
#mongo1 = PyMongo(app, uri="mongodb://localhost:27017/off-top-db")
#@app.route(..) is a decorator. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#It takes a URL rule
app.config['MONGO_DBNAME'] = 'off-top-db' # name of database on mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/off-top-db"
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"
def home_page():
    online_users= mongo1.db.users.find({"online": True})
    return render_template("index.html", online_users= online_users)

if __name__ == "__main__":
  app.run()
