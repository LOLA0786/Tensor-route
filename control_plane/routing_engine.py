from network.registry import get_available_nodes
from control_plane.hardware import compatible
from control_plane.scoring import composite_score
from control_plane.workload import classify_workload
from control_plane.explain import explain_node

last_decision = {}

def select_node(job):
    nodes = get_available_nodes()
    if not nodes:
        return None

    workload_type = classify_workload(job)
    scored_nodes = []

    for node_id, data in nodes.items():
        if compatible(job["gpu_required"], data["gpu"]):
            score = composite_score(node_id, data["gpu"], workload_type)
            explanation = explain_node(node_id, data["gpu"])
            scored_nodes.append((node_id, score, explanation))

    if not scored_nodes:
        return None

    scored_nodes.sort(key=lambda x: x[1], reverse=True)
    chosen = scored_nodes[0]

    global last_decision
    last_decision = {
        "selected_node": chosen[0],
        "score": chosen[1],
        "explanation": chosen[2],
        "workload_type": workload_type,
        "alternatives": [
            {"node": n, "score": s}
            for n, s, _ in scored_nodes[1:]
        ],
    }

    return chosen[0]

def get_last_decision():
    return last_decision
