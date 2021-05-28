#Importing required modules
from flask import Flask, jsonify
from flask import render_template, request
import pandas as pd

# #Create a Flask app
app = Flask(__name__)
# CORS(app)

# import csv
@app.route("/tableau")
def index():
    first_line = True
  
# Return template and data
    return render_template("tableau.html")
     
if __name__ == "__main__":
      app.run(debug=True)