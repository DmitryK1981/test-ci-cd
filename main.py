from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Server Time API")


@app.get("/time")
def get_server_time():
    now = datetime.now(timezone.utc)
    return {
        "utc_time": now.isoformat(),
        "timestamp": now.timestamp(),
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
