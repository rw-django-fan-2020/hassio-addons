ARG BUILD_FROM
FROM $BUILD_FROM

ARG MPC_VERSION
ARG MPD_VERSION
ARG MYMPD_VERSION
ARG UPMPDCLI_VERSION

RUN wget -q -O /tmp/mpd-snapcast.apk \
        https://github.com/rw-django-fan-2020/MPD/releases/download/${MPD_VERSION}/mpd-snapcast.apk && \
    apk add --no-cache --allow-untrusted /tmp/mpd-snapcast.apk && \
    rm /tmp/mpd-snapcast.apk

RUN apk add --no-cache mpc=$MPC_VERSION mympd=$MYMPD_VERSION upmpdcli=$UPMPDCLI_VERSION

ENTRYPOINT [ "/init" ]
CMD []
COPY root /
