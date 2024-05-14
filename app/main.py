from fastapi import FastAPI
from bs4 import BeautifulSoup
from aws_lambda_powertools import Logger
import requests

app = FastAPI()
log = Logger(service="saas-weather-service")

@app.get("/")
async def root():
    log.info("root")
    return {"message": "EC2 Fast API Test"}


@app.get("/weather")
async def weather(location: str):
    log.info("[GET] API: /weather")
    log.info("location: {{}",location)
    # 웹 페이지 가져오기
    html = requests.get('https://search.naver.com/search.naver?query='+location+' 날씨')

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html.text, 'html.parser')

    # 온도 추출
    data_1 = soup.find('div',{'class':'temperature_text'}).text.strip()
    data_2 = soup.find('div',{'class':'temperature_info'}).text.strip()
    data_3 = soup.find('ul',{'class':'today_chart_list'}).text.strip()
    return location + ' ' + data_1, data_2, data_3


@app.get("/health")
async def health():
    log.info("health check")
    return "ok"