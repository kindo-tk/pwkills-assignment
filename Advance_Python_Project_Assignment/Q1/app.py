#1.Build a Flask app that scrapes data from multiple websites and displays it on your site.
# You can try to scrap websites like youtube , amazon and show data on output pages and deploy it on cloud 
#platform .

from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

@app.route("/", methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route("/review", methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            reviews = []
            for commentbox in commentboxes:
                try:
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                except:
                    logging.info("name")

                try:
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'
                    logging.info("rating")

                try:
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except Exception as e:
                    logging.info(e)

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)
                

            return render_template('result.html', reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            logging.error("Error occurred: {}".format(e))
            return 'Something went wrong.'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")