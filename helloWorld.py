#Flask Instance for Off-Top | Flask is a micro-framework

from flask import Flask
app= Flask(__name__)

#@app.route(..) is a decorator. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#It takes a URL rule

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
  app.run()
