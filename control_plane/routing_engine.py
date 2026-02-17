from network.registry import get_available_nodes
from control_plane.hardware import compatible
from control_plane.scoring import composite_score
from control_plane.workload import classify_workload

def select_node(job):
    nodes = get_available_nodes()
    if not nodes:
        return None

    workload_type = classify_workload(job)

    scored_nodes = []

    for node_id, data in nodes.items():
        if compatible(job["gpu_required"], data["gpu"]):
            score = composite_score(node_id, data["gpu"], workload_type)
            scored_nodes.append((node_id, score))

    if not scored_nodes:
        return None

    scored_nodes.sort(key=lambda x: x[1], reverse=True)
    return scored_nodes[0][0]
