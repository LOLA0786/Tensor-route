from network.registry import get_available_nodes
from control_plane.hardware import compatible

def select_node(job):
    nodes = get_available_nodes()
    if not nodes:
        return None

    for node_id, data in nodes.items():
        if compatible(job["gpu_required"], data["gpu"]):
            return node_id

    return None
