#!/usr/bin/env bashio

mkdir -p /share/snapfifo
mkdir -p /share/snapcast
mkdir -p /share/snapserver

if [ "$(bashio::config 'use_custom_config')" == "true" ]; then

    if ! bashio::fs.file_exists '/etc/snapserver.conf'; then
        touch /etc/snapserver.conf ||
            bashio::exit.nok "Could not create snapserver.conf file on filesystem"
    fi

    config=/etc/snapserver.conf
    
    bashio::log.info "Populating snapserver.conf..."

    # Start creation of configuration

    echo "[stream]" > "${config}"
    for source in $(bashio::config 'stream.sources'); do
        echo "source = ${source}" >> "${config}"
    done
    #echo "buffer = $(bashio::config 'stream.buffer')" >> "${config}"
    echo "codec = $(bashio::config 'stream.codec')" >> "${config}"
    echo "send_to_muted = $(bashio::config 'stream.send_to_muted')" >> "${config}"
    echo "sampleformat = $(bashio::config 'stream.sampleformat')" >> "${config}"

    echo "[http]" >> "${config}"
    echo "enabled = $(bashio::config 'http.enabled')" >> "${config}"
    echo "doc_root = $(bashio::config 'http.docroot')" >> "${config}"

    echo "[tcp]" >> "${config}"
    echo "enabled = $(bashio::config 'tcp.enabled')" >> "${config}"

    echo "[logging]" >> "${config}"
    echo "debug = $(bashio::config 'logging.enabled')" >> "${config}"

    echo "[server]" >> "${config}"
    bashio::log.info "threads = $(bashio::config 'server.threads')"
    #echo "threads = $(bashio::config 'server.threads')" >> "${config}"

    echo "[server]" >> "${config}"
    echo "datadir = $(bashio::config 'server.datadir')" >> "${config}"
else 
    if ! bashio::fs.file_exists '/share/snapcast/snapserver.conf'; then
        bashio::log.info "copy /etc/snapserver.conf to /share/snapcast/snapserver.conf"
        cp /etc/snapserver.conf /share/snapcast/snapserver.conf
    fi 

    config=/share/snapcast/snapserver.conf
fi

bashio::log.info "Starting SnapServer..."

/usr/bin/snapserver -c $config