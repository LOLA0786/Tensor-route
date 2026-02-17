from control_plane.metrics import get_system_load
from control_plane.reliability import get_score

BASE_PRICE = 100  # INR per GPU hour baseline

def demand_multiplier():
    load = get_system_load()
    if load == 0:
        return 0.8
    if load < 3:
        return 1.0
    if load < 6:
        return 1.2
    return 1.5

def reliability_multiplier(node_id):
    score = get_score(node_id)
    if score >= 5:
        return 1.2
    if score >= 2:
        return 1.0
    return 0.85

def calculate_price(node_id):
    price = BASE_PRICE * demand_multiplier() * reliability_multiplier(node_id)
    return round(price, 2)
