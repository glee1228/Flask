# -*- coding: utf-8 -*-
# flask run --host 0.0.0.0 --port 8080
from flask import Flask, render_template,request,url_for
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/dh")
def hellojy() :
    return "Hello DH!"
    
@app.route("/donghoon/<string:name>")
def hellodonghoon(name):
    return render_template("hello.html",n=name)
    
@app.route("/christmas")
def christmas() :
    christmas=""
    if datetime.today().strftime("%m%d") =="1225" :
        christmas = "메리 크리스마스~!"
    else :
        christmas = "응 아니야 정신차려~"
        
    return render_template("christmas.html", christmas=christmas)

@app.route("/cube/<int:value>")
def cube(value):
    return render_template("cube.html",n=value*value)
    
@app.route("/lunch")
def lunch():
    lunch_box = ["20층","김밥카페","양자강","바스버거","시골집"]
    lunch = random.choice(lunch_box)
    return render_template("lunch.html",lunch=lunch , box=lunch_box)
    
@app.route("/lucky")
def lucky():
    lucky_num = random.randint(1,100)
    lucky_foodbox = ["가락국수","괴즐레메","군고구마","떡갈비","냉면","김밥","떡볶이","만두","덴뿌라","치킨","염통꼬치","팟타이","호떡"]
    lucky_food = random.choice(lucky_foodbox)
    return render_template("lucky.html",lucky_num=lucky_num,lucky_food = lucky_food,lucky_foodbox=lucky_foodbox)
    
@app.route("/google")
def google():
    return render_template("google.html")
    
@app.route("/opgg")
def opgg():
    return render_template("opgg.html")

@app.route("/opggresult")
def opggresult():
    userName=request.args.get('q')
    url = 'http://www.op.gg/summoner/userName={}'.format(userName)
    
    res = requests.get(url)
    result = BeautifulSoup(res.content, 'html.parser')
    tier = result.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span').text
    gold = "Gold"
    platinum = "Platinum"
    silver = "Silver"
    bronze = "Bronze"
    diamond = "Diamond"
    unranked ="Unranked"
    imgurl = "https://opgg-static.akamaized.net/images/medals/"
    if gold in tier:
        imgurl+="gold_1.png"
    elif platinum in tier:
        imgurl+="platinum_1.png"
    elif silver in tier:
        imgurl+="silver_1.png"
    elif bronze in tier:
        imgurl+="bronze_1.png"
    elif diamond in tier:
        imgurl+="diamond_1.png"
    elif unranked in tier:
        imgurl+="default.png"
    print(imgurl)
    return render_template("opggresult.html",userName=userName,tier=tier,imgurl=imgurl)