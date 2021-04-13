# web-scraping-challenge
Web data extraction was used to extract data from external websites. In this assignment, 4 different websites were scraped and the results are stored in MongoDB. Flask application is then used to render the scraped data to a HTML webpage.

Topics
html5 css-framework flask-application bootstrap3 mongodb-database webscrapping

Web_Scraping-Document-Database
In this assignment, a web application was built that scrapes data from four different websites, to select data related to the Mission to Mars and display the information in a single HTML page.

Scraping:

https://mars.nasa.gov/news/ website was used to get the latest news on Mars mission using BeautifulSoup, splinter, pandas in a jupyter notebook.
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars was used to scrape the featured image of mars in full resolution.
https://space-facts.com/mars/ to gather the facts table about Mars
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to get the images of 4 hemispheres of Mars
Flask:

A python script to run all of the scraping code was designed and all of the scraped data was put into one Python dictionary. Scraping can be updated by the user.

'/scrape' route which will import the Python script and call the scrape function was created.

MongoDB:

A new database and a new collection was created.
All scraped data was stored in the above created database.
The Home route / that will query the database and pass the mars data into HTML template was created.
HTML and BootStrap:

Finally a HTML file called 'index.html' was created that displayed all of the data in HTML elements.
