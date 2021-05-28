#Importing required modules
from flask import Flask, redirect
from flask import render_template, request
import pandas as pd

# #Create a Flask app
app = Flask(__name__)

# Main page
@app.route("/")
def index():
    first_line = True
# Return template and data
    return render_template("index.html")

@app.route("/tableau")
def tableau():
    first_line = True
# Return template and data
    return render_template("tableau.html")

@app.route("/hotel-locator")
def locator():
    first_line = True
# Return template and data
    return render_template("hotellocator.html")

@app.route('/contact')
def contact():
   return render_template("contact.html")


@app.route('/machinel')
def machinel():
    return redirect("https://colab.research.google.com/drive/1YODoeG59I7Z_mmLrhueZD3nqklsoXwQz#scrollTo=4JaEt126iZnc", code=302)

if __name__ == "__main__":
      app.run(debug=True)