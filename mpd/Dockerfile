ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache mpc=0.34-r0
RUN apk add --no-cache mpd=0.23.14-r1
RUN apk add --no-cache ympd=1.3.0-r12

ENTRYPOINT [ "/init" ]
CMD []
COPY root /
