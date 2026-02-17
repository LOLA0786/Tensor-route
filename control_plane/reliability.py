from control_plane.logger import log

scores = {}

def update_score(node_id, success=True):
    s = scores.get(node_id, {"score": 1, "jobs": 0})
    s["jobs"] += 1
    if success:
        s["score"] += 1
    else:
        s["score"] -= 2
    scores[node_id] = s
    log(f"Reliability update {node_id}: {s}")
    return s

def get_score(node_id):
    return scores.get(node_id, {"score":1})["score"]
