from fastapi import FastAPI
from pydantic import BaseModel

from network.registry import register_node, heartbeat
from orchestration.job_queue import add_job
from orchestration.dispatcher import dispatch

app = FastAPI()

class Node(BaseModel):
    node_id: str
    gpu: str
    location: str

class Heartbeat(BaseModel):
    node_id: str

class Job(BaseModel):
    id: str
    gpu_required: str

@app.get("/")
def root():
    return {"status": "TensorRoute control plane running"}

@app.post("/register")
def register(node: Node):
    register_node(node.node_id, node.gpu, node.location)
    return {"status": "registered"}

@app.post("/heartbeat")
def node_heartbeat(hb: Heartbeat):
    heartbeat(hb.node_id)
    return {"status": "alive"}

@app.post("/submit")
def submit(job: Job):
    add_job(job.dict())
    return {"status": "queued"}

@app.post("/dispatch")
def run_dispatch():
    dispatch()
    return {"status": "dispatched"}

from control_plane.metrics import system_metrics

@app.get("/metrics")
def metrics():
    return system_metrics

from control_plane.routing_engine import get_last_decision

@app.get("/decision")
def decision():
    return get_last_decision()
