ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG C.UTF-8

#Install snapcast
ARG SNAPCAST_VERSION
RUN apk add --no-cache snapcast-server=$SNAPCAST_VERSION bash



# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]