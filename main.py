from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Server Time API")


@app.get("/time")
def get_server_time():
    now = datetime.now(timezone.utc)
    return {
        "time": now.strftime("%H:%M:%S"),
    }


@app.get("/date")
def get_server_date():
    now = datetime.now(timezone.utc)
    return {
        "date": now.strftime("%Y-%m-%d"),
    }


@app.get("/datetime")
def get_server_datetime():
    now = datetime.now(timezone.utc)
    return {
        "utc_datetime": now.isoformat(),
        "timestamp": now.timestamp(),
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
