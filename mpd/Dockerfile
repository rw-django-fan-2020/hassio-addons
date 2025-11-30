ARG BUILD_FROM
FROM $BUILD_FROM

ARG MPC_VERSION
ARG MPD_VERSION
ARG MYMPD_VERSION
ARG UPMPDCLI_VERSION

#https://build.alpinelinux.org/buildlogs/build-3-22-aarch64/community/mpd/mpd-0.24.5-r0.log
RUN apk add --no-cache git \
    build-base \
    alsa-lib-dev \
    avahi-dev \
    curl-dev \
    expat-dev \
    faad2-dev \
    ffmpeg-dev \
    flac-dev \
    fmt-dev \
    glib-dev \
    gtest-dev \
    icu-dev \
    jack-dev \
    lame-dev \
    libao-dev \
    libcap-utils \
    libcdio-paranoia-dev \
    libid3tag-dev \
    libmad-dev \
    libmodplug-dev \
    libmpdclient-dev \
    libnfs-dev \
    libogg-dev \
    libsamplerate-dev \
    libshout-dev \
    libvorbis-dev \
    meson \
    opus-dev \
    pipewire-dev \
    pulseaudio-dev \
    py3-attrs \
    py3-sphinx \
    py3-sphinx_rtd_theme \
    libupnp-dev \
    mpc=$MPC_VERSION \
    #mpd=$MPD_VERSION \
    mympd=$MYMPD_VERSION \
    upmpdcli=$UPMPDCLI_VERSION

RUN git clone https://github.com/MusicPlayerDaemon/MPD.git /tmp/mpd \
    && cd /tmp/mpd \
    && git fetch --tags \
    && git checkout $MPD_VERSION \
    && meson setup . output/release \
        --buildtype=release \
        --prefix=/usr \
        -Dsysconfdir='/etc' \
    && ninja -C output/release \
    && ninja -C output/release install \
    && rm -rf /tmp/mpd

RUN apk del build-base meson ninja git pkgconfig \
    && rm -rf /var/cache/apk/*

ENTRYPOINT [ "/init" ]
CMD []
COPY root /
