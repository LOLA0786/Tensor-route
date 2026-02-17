from network.registry import get_available_nodes
from control_plane.reliability import get_score

def select_node(job):
    nodes = get_available_nodes()
    if not nodes:
        return None

    ranked = sorted(
        nodes.items(),
        key=lambda x: get_score(x[0]),
        reverse=True
    )

    return ranked[0][0]
