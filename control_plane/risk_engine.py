from control_plane.data_moat import node_performance

def reliability_score(node_id):
    node = node_performance.get(node_id)
    if not node or node["jobs"] == 0:
        return 0.8

    failure_rate = node["failures"] / node["jobs"]

    if failure_rate < 0.02:
        return 0.99
    elif failure_rate < 0.05:
        return 0.95
    elif failure_rate < 0.1:
        return 0.90
    else:
        return 0.75

def insurance_risk_multiplier(node_id):
    score = reliability_score(node_id)

    if score > 0.98:
        return 1.0
    elif score > 0.95:
        return 1.1
    elif score > 0.90:
        return 1.25
    return 1.5
