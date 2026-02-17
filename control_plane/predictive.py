from control_plane.metrics import system_metrics

def congestion_risk():
    load = system_metrics["active_jobs"]

    if load < 2:
        return "low"
    if load < 5:
        return "moderate"
    return "high"

def reliability_risk(node_score):
    if node_score > 0.98:
        return "low"
    if node_score > 0.9:
        return "moderate"
    return "high"
