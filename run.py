uvicorn src.main:app --port=${PORT:-10000} --host=${HOST:-"0.0.0.0"} --log-config=logs/logging.ini --no-access-log
