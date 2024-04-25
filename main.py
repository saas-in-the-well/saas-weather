from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "EC2 Fast API Test"}


@app.get("/weather")
async def weather(location: str):

    # 웹 페이지 가져오기
    html = requests.get('https://search.naver.com/search.naver?query='+location+' 날씨')

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html.text, 'html.parser')

    # 온도 추출
    data_1 = soup.find('div',{'class':'temperature_text'}).text.strip()
    data_2 = soup.find('div',{'class':'temperature_info'}).text.strip()
    data_3 = soup.find('ul',{'class':'today_chart_list'}).text.strip()
    return location + ' ' + data_1, data_2, data_3