from collections import defaultdict
import time

workload_profiles = defaultdict(lambda: {
    "runs": 0,
    "avg_duration": 0,
    "failures": 0,
    "gpu_type_usage": defaultdict(int),
})

node_performance = defaultdict(lambda: {
    "jobs": 0,
    "failures": 0,
    "avg_runtime": 0,
})

pricing_signals = {
    "accepted_prices": [],
    "rejected_prices": [],
    "demand_spikes": [],
}

def fingerprint_workload(job, duration, success, gpu_type):
    profile = workload_profiles[job["id"]]

    profile["runs"] += 1
    profile["avg_duration"] = (
        (profile["avg_duration"] * (profile["runs"] - 1) + duration)
        / profile["runs"]
    )
    profile["gpu_type_usage"][gpu_type] += 1

    if not success:
        profile["failures"] += 1

def record_node_performance(node_id, duration, success):
    node = node_performance[node_id]
    node["jobs"] += 1
    node["avg_runtime"] = (
        (node["avg_runtime"] * (node["jobs"] - 1) + duration)
        / node["jobs"]
    )
    if not success:
        node["failures"] += 1

def record_price_signal(price, accepted=True):
    key = "accepted_prices" if accepted else "rejected_prices"
    pricing_signals[key].append(price)

def record_demand_spike(load):
    pricing_signals["demand_spikes"].append({
        "load": load,
        "time": time.time()
    })
