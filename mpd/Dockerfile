ARG BUILD_FROM
FROM $BUILD_FROM

ARG mpc_version
ENV mpc_version=${mpc_version}

#https://pkgs.alpinelinux.org/packages?name=mpc&branch=v3.19&repo=&arch=&maintainer=
#https://pkgs.alpinelinux.org/packages?name=mpd&branch=v3.19&repo=&arch=&maintainer=
#https://pkgs.alpinelinux.org/packages?name=ympd&branch=v3.19&repo=&arch=&maintainer=
RUN apk add --no-cache mpc=$mpc_version mpd=0.23.14-r1 ympd=1.3.0-r12

ENTRYPOINT [ "/init" ]
CMD []
COPY root /
