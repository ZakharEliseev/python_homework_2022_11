from fastapi import FastAPI
from views.ping import router as ping_router
app = FastAPI()
app.include_router(ping_router)


@app.get("/")
def root():
    ping = 'http://0.0.0.0:8000/ping/'
    return ping

