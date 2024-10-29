
FROM python

EXPOSE 8080

RUN apt-get update && \
    apt-get install -y build-essential python3-distutils && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
