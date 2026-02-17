from orchestration.job_queue import get_job
from control_plane.routing_engine import select_node
from control_plane.logger import log

def dispatch():
    job = get_job()
    if not job:
        return

    node = select_node(job)

    if node:
        log(f"Dispatching job {job['id']} to {node}")
    else:
        log("No nodes available")
