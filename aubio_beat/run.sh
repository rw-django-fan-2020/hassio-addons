#!/bin/bash
export FIFO_PATH="${FIFO_PATH:-/share/beat_fifo}"
export LOG_LEVEL="${LOG_LEVEL:-DEBUG}"

echo "[INFO] Starting Beat Detection Add-on"
echo "[INFO] FIFO path: $FIFO_PATH"
echo "[INFO] Log level: $LOG_LEVEL"

python3 /app/beat_service.py
