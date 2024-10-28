FROM  python:3.7.8-slim

EXPOSE 8080

RUN pip install -U pip 

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requeriments.txt

COPY . /app
WORKDIR /app


ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port= 8080" , "--server.address=0.0.0.0"]