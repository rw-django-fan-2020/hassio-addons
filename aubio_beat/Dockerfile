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
 && pip install --no-cache-dir pyyaml \
 && apt-get purge -y build-essential python3-dev gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY run.sh /run.sh
COPY beat_service.py /app/beat_service.py
RUN chmod +x /run.sh

CMD [ "/run.sh" ]