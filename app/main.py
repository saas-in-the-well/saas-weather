import logging

from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import boto3
import time

app = FastAPI()

# # CloudWatch Logs 클라이언트 생성
# logs = boto3.client('logs')
#
# # 로그 그룹 생성
# log_group_name = '/aws/devops/saas/weather-log'
# logs.create_log_group(logGroupName=log_group_name)
#
# # 로그 스트림 생성
# log_stream_name = 'saas-weather-app-stream'
# logs.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
#
# # 로그 이벤트 전송
# log_events = [
#     {
#         'timestamp': int(time.time() * 1000),
#         'message': 'This is a log message.'
#     }
# ]
# logs.put_log_events(
#     logGroupName=log_group_name,
#     logStreamName=log_stream_name,
#     logEvents=log_events
#)

@app.get("/")
async def root():
    #logs.info("root")
    return {"message": "EC2 Fast API Test"}


@app.get("/weather")
async def weather(location: str):
    #logs.info("[GET] API: /weather")
    #logs.info("location: {{}",location)
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
    #logs.info("health check")
    return "ok"