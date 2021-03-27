#from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
#from datetime import datetime
#import pymongo
#from jinja2 import Template
#import pandas as pd
#import json
#import scrape_mars
#from bs4 import BeautifulSoup
#import pymongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd
from bs4 import BeautifulSoup


app = Flask(__name__)

#conn = "mongodb://localhost:27017"
#conn = "mongodb://localhost:27017"
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_db")

@app.route("/")
def home():
    #mars_db = client.mars
    mars_data = mongo.db.mars_collection.find_one()
    print(mars_data)
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    # Run scrape function
    mars_data = scrape_mars.results  #scrape_mars.scrape_info()
    #mars_data = scrape_mars.scrape_info()
    #Update Mongo database
    mongo.db.mars_collection.update({},mars_data, upsert=True)

    #Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)