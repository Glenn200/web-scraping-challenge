{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "from flask import Flask, render_template, jsonify, redirect\n",
    "import pymongo\n",
    "import scrape_mars\n",
    "\n",
    "sys.setrecursionlimit(2000)\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "client = pymongo.MongoClient()\n",
    "db = client.mars_db\n",
    "collection = db.mars_facts\n",
    "\n",
    "\n",
    "\n",
    "@app.route('/scrape')\n",
    "def scrape():\n",
    "   # db.collection.remove()\n",
    "    mars = scrape_mars.scrape()\n",
    "    print(\"\\n\\n\\n\")\n",
    "    #print(mars)\n",
    "    #mars = {'news_title': \"NASA's Next Mars Lander Spreads its Solar Wings\", 'news_paragraph': \"NASA's next mission to Mars passed a key test Tuesday, extending the solar arrays that will power the InSight spacecraft once it lands on the Red Planet this November.\", 'featured_image': 'https://www.jpl.nasa.gov//spaceimages/images/largesize/PIA20318_hires.jpg', 'mars_weather': 'Sol 1945 (Jan 25, 2018), Sunny, high -22C/-7F, low -78C/-108F, pressure at 7.51 hPa, daylight 05:43-17:28', 'hemisphere_img_url': [{'image title': 'Cerberus Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}, {'image title': 'Schiaparelli Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}, {'image title': 'Syrtis Major Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}, {'image title': 'Valles Marineris Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}]}\n",
    "    db.mars_facts.insert_one(mars)\n",
    "    return \"Some scrapped data\"\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    mars = list(db.mars_facts.find())\n",
    "    print(mars)\n",
    "    return render_template(\"index.html\", mars = mars)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
