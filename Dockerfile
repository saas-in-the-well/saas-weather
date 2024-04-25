FROM python:3.9

WORKDIR /weather_test

COPY ./requirements.txt /weather_test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /weather_test/requirements.txt

COPY ./app /weather_test/app

WORKDIR /weather_test/app

EXPOSE 7070

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7070"]