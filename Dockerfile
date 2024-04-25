# 베이스 이미지를 지정합니다.
FROM python:3.8-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 호스트의 소스 코드를 Docker 이미지로 복사합니다.
COPY . /app

# 필요한 종속성을 설치합니다.
RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install -r requirements.txt \
RUN pip install uvicorn

# 애플리케이션을 실행합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]

