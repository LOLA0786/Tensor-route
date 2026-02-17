from orchestration.job_queue import get_job
from control_plane.routing_engine import select_node
from control_plane.logger import log
from control_plane.metrics import start_job, finish_job
from control_plane.pricing import calculate_price
import time

def dispatch():
    job = get_job()
    if not job:
        log("No jobs in queue")
        return

    node = select_node(job)

    if not node:
        log("No nodes available")
        return

    price = calculate_price(node)

    log(f"Dispatching job {job['id']} to {node}")
    log(f"Spot price: ₹{price} / GPU-hour")

    start_job(node)
    time.sleep(5)   # simulate real workload
    finish_job(node, success=True)

    log(f"Job {job['id']} completed")
