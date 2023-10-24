FROM python:3.7-alpine

WORKDIR /app
COPY . /app
EXPOSE 8080

CMD ["python", "main.py"]
