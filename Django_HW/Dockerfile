FROM python:3.11

WORKDIR /data

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000