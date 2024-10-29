FROM python:3.7.8-slim

EXPOSE 8080

#RUN apt-get update && \
 #   apt-get install -y build-essential python3-distutils python3-pip && \
  #  rm -rf /var/lib/apt/lists/*
#RUN pip install setuptools
#RUN pip install build

RUN pip install --upgrade pip 

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
