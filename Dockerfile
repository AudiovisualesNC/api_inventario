FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /home/av

ENV MYSQL_HOST=db
ENV MYSQL_USER=user
ENV MYSQL_PASS=password
ENV MYSQL_DB=db

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ../../Desktop/inventario /app/app
