supplier_stats = {}

def record_supplier_activity(node_id, earned, job_completed=True):
    s = supplier_stats.setdefault(node_id, {
        "earnings": 0,
        "jobs_completed": 0,
        "uptime_contribution": 0,
    })

    s["earnings"] += earned
    if job_completed:
        s["jobs_completed"] += 1

def liquidity_score(node_id):
    s = supplier_stats.get(node_id)
    if not s:
        return 0

    return s["jobs_completed"] * 0.7 + s["earnings"] * 0.3
