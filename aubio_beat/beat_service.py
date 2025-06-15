import logging
import os
import aubio
import numpy as np
from flask import Flask, jsonify
import threading

# Logging einrichten
log_level = os.environ.get("LOG_LEVEL", "DEBUG").upper()
numeric_level = getattr(logging, log_level, logging.DEBUG)
logging.basicConfig(level=numeric_level, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("beat-addon")

app = Flask(__name__)
last_beat = {'volume': 0.0}

def process_fifo():
    fifo_path = os.environ.get("FIFO_PATH", "/share/beat_fifo")
    if not os.path.exists(fifo_path):
        logger.info(f"FIFO not found at {fifo_path}, creating it...")
        os.mkfifo(fifo_path)
    else:
        logger.info(f"Using existing FIFO at {fifo_path}")

    try:
        with open(fifo_path, 'rb', buffering=0) as f:
            win_s = 1024
            hop_s = win_s // 2
            samplerate = 44100
            beat_o = aubio.tempo("default", win_s, hop_s, samplerate)
            logger.info("Started beat detection loop")

            while True:
                data = f.read(win_s * 2)
                if not data:
                    continue
                samples = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
                is_beat = beat_o(samples)
                volume = float(np.sqrt(np.mean(samples**2)))
                if is_beat:
                    last_beat['volume'] = volume
                    logger.debug(f"Beat detected, volume: {volume:.4f}")
    except Exception as e:
        logger.exception(f"Error in FIFO processing: {e}")

@app.route('/beat', methods=['GET'])
def beat():
    logger.debug("GET /beat called")
    return jsonify(last_beat)

if __name__ == "__main__":
    threading.Thread(target=process_fifo, daemon=True).start()
    try:
        logger.info("Starting Flask server on 0.0.0.0:5000")
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        logger.exception(f"Flask server crashed: {e}")
