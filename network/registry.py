import time

nodes = {}

HEARTBEAT_TIMEOUT = 60  # seconds

def register_node(node_id, gpu_type, location):
    nodes[node_id] = {
        "gpu": gpu_type,
        "location": location,
        "last_seen": time.time(),
        "status": "online",
        "reliability": 1.0,
    }

def heartbeat(node_id):
    if node_id in nodes:
        nodes[node_id]["last_seen"] = time.time()
        nodes[node_id]["status"] = "online"

def get_available_nodes():
    now = time.time()

    for node_id, data in nodes.items():
        if now - data["last_seen"] > HEARTBEAT_TIMEOUT:
            data["status"] = "offline"

    return {
        k: v for k, v in nodes.items()
        if v["status"] == "online"
    }
