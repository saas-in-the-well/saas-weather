FROM python:3.7

COPY . /app
WORKDIR /app
ENV PYTHONPATH /app
ENV PYTHONBUFFERED=1

# layer를 하나로 묶음 layer가 늘어나면 보통 안좋음
RUN pip install pip==21.2.4 && \
    pip install -r requirements.txt
    
CMD ["saas-weather-application-0.0.1-SNAPSHOT", "main.py"]