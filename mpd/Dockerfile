ARG BUILD_FROM
FROM $BUILD_FROM

ARG MPC_VERSION
ARG MPD_VERSION
ARG YMPD_VERSION

RUN apk add --no-cache mpc=$MPC_VERSION mpd=$MPD_VERSION ympd=$YMPD_VERSION

ENTRYPOINT [ "/init" ]
CMD []
COPY root /
