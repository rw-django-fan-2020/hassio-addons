ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

RUN pip install --no-cache-dir \
    nostr-sdk \
    requests \
    pyyaml

COPY app/ /app/
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
