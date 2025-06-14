#!/bin/bash
export FIFO_PATH="${FIFO_PATH:-/share/beat_fifo}"

python3 <<EOF
from flask import Flask, jsonify
import aubio
import numpy as np
import os

app = Flask(__name__)
last_beat = {'volume': 0}

def process_fifo():
    if not os.path.exists('$FIFO_PATH'):
        os.mkfifo('$FIFO_PATH')
    f = open('$FIFO_PATH', 'rb', buffering=0)
    win_s = 1024
    hop_s = win_s // 2
    samplerate = 44100
    beat_o = aubio.tempo("default", win_s, hop_s, samplerate)
    while True:
        data = f.read(win_s * 2)
        if not data:
            continue
        samples = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
        is_beat = beat_o(samples)
        volume = np.sqrt(np.mean(samples**2))
        if is_beat:
            last_beat['volume'] = volume

@app.route('/beat', methods=['GET'])
def beat():
    return jsonify(last_beat)

import threading
threading.Thread(target=process_fifo, daemon=True).start()
app.run(host="0.0.0.0", port=5000)
EOF