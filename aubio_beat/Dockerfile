FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libaubio-dev \
    libsndfile1 \
    build-essential \
    python3-dev \
    pkg-config \
 && pip install --no-cache-dir numpy \
 && pip install --no-cache-dir flask aubio \
 && apt-get purge -y build-essential python3-dev gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
