FROM python:3.11-slim

# Set environment vars to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libaubio-dev \
        libsndfile1 \
        build-essential \
        python3-dev \
        libffi-dev \
        libasound2-dev \
        pkg-config \
    && pip install --no-cache-dir flask aubio \
    && apt-get purge -y --auto-remove gcc build-essential python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
