from python:3.7.8-slim

EXPOSE 8080

RUN pip install -U pip 

copy requeriments.txt app/requeriments.txt
run pip install -r app/requeriments.txt

copy . /app
WORKDIR /app


ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port= 8080" , "--server.address=0.0.0.0"]