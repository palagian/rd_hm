FROM python:3.11

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

COPY app.py /app
COPY templates /app/templates

ENV FLASK_APP=app.py

EXPOSE 4200

CMD ["gunicorn", "-b", "0.0.0.0:4200", "app:app"]
