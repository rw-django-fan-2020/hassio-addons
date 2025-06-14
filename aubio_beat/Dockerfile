FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      gcc build-essential pkg-config \
      libaubio-dev libsndfile1 \
      python3-dev \
    && pip install --no-cache-dir flask aubio \
    && apt-get purge -y build-essential python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
