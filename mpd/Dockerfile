ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache mpc=0.35-r0
RUN apk add --no-cache mpd=0.23.15-r2
RUN apk add --no-cache ympd=1.3.0-r9

ENTRYPOINT [ "/init" ]
CMD []
COPY root /
