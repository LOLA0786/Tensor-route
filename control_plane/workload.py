def classify_workload(job):
    if job.get("type") == "inference":
        return "inference"
    if job.get("latency_sensitive"):
        return "inference"
    return "training"
