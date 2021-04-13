from flask import Flask, render_template, redirect, request 
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd
from bs4 import BeautifulSoup
import pymongo

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():
    #mars_db = client.mars
    mars_data = mongo.db.collection.find_one()
    try:
        print(mars_data["hemisphere_image_urls"][0]["img_url"])
    # Trap Error when no data returned. Create dummy data.
    except (TypeError):
        mars_data = []
        hemisphere_image_urls = []
        hemisphere_image_urls.append({"title": "","img_url":""})
        hemisphere_image_urls.append({"title": "","img_url":""})
        hemisphere_image_urls.append({"title": "","img_url":""})
        hemisphere_image_urls.append({"title": "","img_url":""})
        mars_data = {
            'news_title': '(TBD) - Press "Scrape New Data Button for latest information',
            'news_p': '',
            'featured_image_url': '',
            'mars_table_html_string': '',
            'hemisphere_image_urls' : hemisphere_image_urls    
        }
        print("Null entry created")
  
    #print(mars_data)
    return render_template("index.html",mars=mars_data)

@app.route("/scrape")
def scrape():
    # Run scrape function
    mars_data = scrape_mars.scrape_info()
    #Update Mongo database
    mongo.db.collection.update({}, mars_data, upsert=True)

    #Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)