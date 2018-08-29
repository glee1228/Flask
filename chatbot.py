import os
import requests
# 1. api 사용 기본 url 설정
# $ vi ~/. bashrc 해서 bashrc 설정 파일을 열어서
# export TELEGRAM_TOKEN=token....

token = "649591240:AAHTQvj-Edq7zUyjtIN-oHS8kyccQ_7oBSk"
base_url = "https://api.telegram.org/bot{}/".format(token)

# 2. chat_id를 받아오는 코드
#~~~~~/getUpdates 요청을 보내시고
#json에서 chat_id 값을 뽑아오시면 됩니다.
res = requests.get(base_url+"getUpdates").json()
print(res)
print(res["result"])

print(res["result"][0]["message"]["from"]["id"])

chat_id = res["result"][0]["message"]["from"]["id"]

# 3. 크롤링
usl = ""

 #3. 메세지 보내는 코드
msg = "안녕하세요?"
msg_url = "sendMessage?chat_id={}&text={}".format(chat_id,msg)
print(requests.get(base_url+msg_url))