FROM python:3.7

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 7000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7000"]