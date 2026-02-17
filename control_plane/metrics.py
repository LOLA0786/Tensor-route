import time

node_metrics = {}
system_metrics = {
    "jobs_completed": 0,
    "jobs_failed": 0,
    "active_jobs": 0,
}

def start_job(node_id):
    node = node_metrics.setdefault(node_id, {
        "jobs": 0,
        "failures": 0,
        "gpu_seconds": 0,
        "start_time": None,
    })
    node["start_time"] = time.time()
    system_metrics["active_jobs"] += 1

def finish_job(node_id, success=True):
    now = time.time()
    node = node_metrics[node_id]

    duration = now - node["start_time"]
    node["gpu_seconds"] += duration
    node["jobs"] += 1

    if not success:
        node["failures"] += 1
        system_metrics["jobs_failed"] += 1
    else:
        system_metrics["jobs_completed"] += 1

    system_metrics["active_jobs"] -= 1

def get_node_utilization(node_id):
    node = node_metrics.get(node_id)
    if not node or node["jobs"] == 0:
        return 0
    return node["gpu_seconds"] / node["jobs"]

def get_system_load():
    return system_metrics["active_jobs"]
