ARG BUILD_FROM
FROM $BUILD_FROM as BUILDER

ARG BUILD_VERSION
ARG BUILD_ARCH
ENV LANG C.UTF-8
ENV SNAPCAST_VERSION 0.27.0

COPY qemu-arm-static /usr/bin/qemu-arm-static
COPY qemu-aarch64-static /usr/bin/qemu-aarch64-static

RUN if [ "$BUILD_ARCH" = "armhf" -o "$BUILD_ARCH" = "armv7" ]; then rm /usr/bin/qemu-aarch64-static;\
    elif [ "$BUILD_ARCH" = "aarch64" ]; then rm /usr/bin/qemu-arm-static;\
    fi

#RUN Install 1
RUN set -ex \
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    # Official Mopidy install for Debian/Ubuntu along with some extensions
    # (see https://docs.mopidy.com/en/latest/installation/debian/ )
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	build-essential \
        curl \
        gcc

RUN set -ex \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	gstreamer1.0-alsa \
	gstreamer1.0-fluendo-mp3 \
	gstreamer1.0-libav

RUN set -ex \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	libxml2-dev \
	libxslt-dev \
	libz-dev \
	jq \
	python-crypto \
	python-dev

#RUN Install 2
RUN set -ex \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 && curl -L https://apt.mopidy.com/mopidy.gpg -o /tmp/mopidy.gpg \
 && curl -L https://apt.mopidy.com/mopidy.list -o /etc/apt/sources.list.d/mopidy.list \
 && apt-key add /tmp/mopidy.gpg \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        jq mopidy mopidy-spotify mopidy-local-sqlite \
 && curl -L https://bootstrap.pypa.io/get-pip.py | python - \
 && pip install -U six oauth2client pyasn1 \
 && pip install \
	Mopidy-Moped \
        Mopidy-GMusic \
	Mopidy-Iris \
 && apt-get purge --auto-remove -y \
#        curl \
        gcc \
#	build-essential \
# && apt-get clean \
# && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#RUN Install 3
RUN set -ex \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
# && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        curl jq git build-essential \
		libasound2-dev libvorbisidec-dev libvorbis-dev libflac-dev alsa-utils libavahi-client-dev avahi-daemon \
#	build-essential \
	debhelper dh-make dh-systemd quilt fakeroot lintian \
 && cd /tmp/ \
 && git clone https://github.com/badaix/snapcast.git \
 && cd snapcast \
 && git checkout v${SNAPCAST_VERSION} \
 && cd externals \
 && git submodule update --init --recursive
RUN cd /tmp/snapcast/server \
 && make dpkg \
 && mv $(ls ../snapserver*.deb) /snapserver.deb

ARG BUILD_FROM
FROM $BUILD_FROM

ARG BUILD_ARCH

#ENV LANG C.UTF-8
COPY --from=BUILDER /snapserver.deb /tmp/
#Install snapcast-server
RUN set -ex \
    # Official Mopidy install for Debian/Ubuntu along with some extensions
    # (see https://docs.mopidy.com/en/latest/installation/debian/ )
 && apt-get update \
 && dpkg -i /tmp/snapserver.deb || DEBIAN_FRONTEND=noninteractive apt-get install -f -y\
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache

COPY mopidy_cast.conf /var/lib/mopidy/.config/mopidy/mopidy_cast.conf

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

EXPOSE 6600 6680 1704 1705


CMD [ "/run.sh" ]
