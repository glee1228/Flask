## Flask로 로직처리하기

app.py  

```python
r# -*- coding: utf-8 -*-
# flask run --host 0.0.0.0 --port 8080
from flask import Flask, render_template,request
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
    
    return render_template("opggresult.html",userName=userName,tier=tier)
```



## LayOut 만들기

layout.html

<!Doctype html>
<! --html:5-->
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

```html
  <!Doctype html>
<! --html:5-->
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

        <title>{%block title %}{% endblock %}</title>
    </head>
    <body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/christmas">크리스마스</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/lucky">오늘의 행운</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/lunch">점심메뉴 추천</a>
            </li>
        </ul>
    </div>
</nav>
        {%block body %}
        {% endblock %}
        <a href="/lunch" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">점심메뉴 추천</a>
        <a href="/christmas" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">크리스마스일까?</a>
        <a href="/lucky" class="btn btn-success btn-lg active" role="button" aria-pressed="true">오늘의 행운</a>
        
    </body>
</html>
```
<hr/>

Layout2.html

<!Doctype html>
<! --html:5-->
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

```html
<!Doctype html>
<! --html:5-->
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

        <title>{%block title %}{% endblock %}</title>
    </head>
    <body>

        {%block body %}
        {% endblock %}
       
    </body>
</html>
```
<hr/>

## 크리스마스 확인 및 점심메뉴추천 및 행운 숫자 뽑기 

lucky.html

``` html
{% extends "layout.html" %}
{% block title %} 오늘의 행운 고르기 {% endblock %}

{% block body%}
    <h1>오늘의 행운의 숫자 : {{lucky_num}}</h1>
    <hr/>
    <h1>오늘의 행운의 음식 : {{lucky_food}}</h1>
    {% for menu in lucky_foodbox %}
    <h3>{{menu}}</h3>
    <hr/>
    {% endfor %}
    
    
{% endblock %}
```



<hr/>

lunch.html


```html
{% extends "layout.html" %}
{% block title %}점심 메뉴 추천 {% endblock %}

{% block body%}
    <h1>{{lunch}} 먹으러간다~</h1>
    <hr/>
        {% for menu in box %}
        <p>{{menu}}</p>
        {% endfor %}
    <hr/>
    
{% endblock %}
```


<hr/>

christmas.html

``` html
{% extends "layout.html" %}
{% block title %} 크리스마스? {% endblock %}

{% block body%}
    <h1>{{christmas}}</h1>
    <hr/>
    <br><br>
    
    
    
{% endblock %}
```


<hr/>

## OP.GG 크롤링하여 가짜 OP.GG 만들기

opgg.html

```html
{% extends "layout2.html" %}
{% block title %} 구글 {% endblock %}
{% block body %} 
<h1 class="text-center">OPGG</h1>
<form class="text-center" style="" action="/opggresult">
    소환사 명 검색 : <input type="text" name="q" value="">
    <input type="submit" value ="뿅!!!">
</form>
{% endblock %}
```



<hr/>

opggresult.html

```html
{% extends "layout2.html" %}
{% block title %} 구글 {% endblock %}
{% block body %} 
<h1 class="text-center">{{userName}} 소환사님</h1>
<h2 class="text-center">{{tier}} 티어 입니다.</h2>

{% endblock %}
```



<hr/>

