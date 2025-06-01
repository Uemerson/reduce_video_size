FROM python:3.13-alpine

RUN apk add --no-cache \
    ffmpeg \
    bash

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir ffmpeg-python

CMD ["python", "main.py"]
