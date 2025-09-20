Production Ready Dockerized Flask API

## Run with Docker
'''bash
docker build -t flask-api-prod .
docker run -p 5000:5000 flask-api-prod

## Run with Docker Compose
docker compose up --build

## Test
In another terminal, run:

curl.exe -X POST http://localhost:5000/add -H "Content-Type: application/json" -d "{\"num1\":x,\"num2\":y}"

