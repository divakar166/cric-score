from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/featuredData')
def get_data():
    URL = "https://www.cricbuzz.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    results = soup.find(id="match_menu_container")
    scrap_result = results.find_all("div",class_="cb-pos-rel")
    data = []
    for i in range(0,len(scrap_result)):
        data.append(scrap_result[i].prettify())
    return data

if __name__ == '__main__':
    app.run()