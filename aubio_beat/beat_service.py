import logging
import os
import aubio
import numpy as np
from flask import Flask, jsonify
import threading
import yaml

# 1. Setze log_level und fifo_path
log_level = "DEBUG"
fifo_path = "/share/snapfifo/snapfifo"
#log_level = os.environ.get("LOG_LEVEL").upper()
#if not log_level:
#    raise ValueError("LOG_LEVEL is not set. Please check add-on config.")

#fifo_path = os.environ.get("FIFO_PATH")
#if not fifo_path:
#    raise ValueError("FIFO_PATH is not set. Please check add-on config.")


# Logging einrichten
numeric_level = getattr(logging, log_level, logging.DEBUG)
logging.basicConfig(level=numeric_level, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("beat-addon")

app = Flask(__name__)
last_beat = {'volume': 0.0}

def process_fifo():
    logger.info(f"Using FIFO path: {fifo_path}")
    
    if not os.path.exists(fifo_path):
        logger.info("FIFO does not exist, creating it...")
        os.mkfifo(fifo_path)

    try:
        with open(fifo_path, 'rb', buffering=0) as f:
            win_s = 1024
            hop_s = 512  # aubio.tempo expects hop_s-sized input
            samplerate = 44100
            beat_o = aubio.tempo("default", win_s, hop_s, samplerate)

            logger.info("Starting beat detection loop...")
            while True:
                data = f.read(hop_s * 2)  # int16 = 2 bytes per sample
                if not data or len(data) < hop_s * 2:
                    continue
                samples = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
                try:
                    is_beat = beat_o(samples)
                    volume = np.sqrt(np.mean(samples**2))
                    if is_beat:
                        logger.debug(f"Beat detected! Volume: {volume}")
                        # Update global or shared state here
                except Exception as e:
                    logger.error(f"Error in beat processing: {e}")
    except Exception as e:
        logger.exception(f"Error opening FIFO: {e}")


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
