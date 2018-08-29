import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise'
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
kospi = result.select_one('#KOSPI_now')
kospi = kospi.select_one('#')
print('현재 코스피 지수는 {}입니다.'.format(kospi))

