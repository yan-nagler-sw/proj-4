FROM python:3-slim

RUN pip install pymysql
RUN pip install flask

WORKDIR /app

COPY rest_app.py ./
COPY db_connector.py ./
COPY backend_testing_db.py ./

EXPOSE 30000/tcp

CMD python3 rest_app.py
