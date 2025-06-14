FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y gcc libaubio-dev libsndfile1 && \
    pip install flask aubio

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]