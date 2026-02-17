from control_plane.data_moat import node_performance

def reputation_score(node_id):
    node = node_performance.get(node_id)
    if not node:
        return 0.5

    success_rate = 1 - (node["failures"] / node["jobs"]) if node["jobs"] else 0.5

    if success_rate > 0.98:
        return 1.0
    if success_rate > 0.95:
        return 0.9
    if success_rate > 0.9:
        return 0.75
    return 0.5
