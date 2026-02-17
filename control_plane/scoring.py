from control_plane.pricing import calculate_price
from control_plane.risk_engine import reliability_score
from control_plane.hardware import get_gpu_score
from control_plane.metrics import get_system_load

def composite_score(node_id, gpu_type, workload_type):
    price = calculate_price(node_id)
    reliability = reliability_score(node_id)
    performance = get_gpu_score(gpu_type)

    latency_factor = 1 / (1 + get_system_load())

    if workload_type == "inference":
        perf_weight = 0.4
        latency_weight = 0.4
        cost_weight = 0.2
    else:  # training
        perf_weight = 0.5
        latency_weight = 0.1
        cost_weight = 0.4

    score = (
        perf_weight * performance +
        latency_weight * latency_factor +
        cost_weight * (1 / price) +
        reliability * 0.3
    )

    return score
