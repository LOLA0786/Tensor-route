import time
import requests
import socket

SERVER = "http://localhost:8000/register"

node_id = socket.gethostname()

def register():
    requests.post(SERVER, json={
        "node_id": node_id,
        "gpu": "A100",
        "location": "India"
    })

while True:
    register()
    time.sleep(60)
