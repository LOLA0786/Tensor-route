from control_plane.pricing import calculate_price
from control_plane.risk_engine import reliability_score
from control_plane.hardware import get_gpu_score
from control_plane.metrics import get_system_load
from control_plane.predictive import congestion_risk

def explain_node(node_id, gpu_type):
    price = calculate_price(node_id)
    reliability = reliability_score(node_id)
    performance = get_gpu_score(gpu_type)
    congestion = congestion_risk()

    return {
        "price_per_hour": price,
        "reliability_score": reliability,
        "performance_score": performance,
        "congestion_level": congestion,
        "cost_efficiency": round(performance / price, 4),
    }
