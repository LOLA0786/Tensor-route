import time
import requests
import socket

SERVER = "http://localhost:8000/heartbeat"
node_id = socket.gethostname()

while True:
    requests.post(SERVER, json={"node_id": node_id})
    time.sleep(30)
