GPU_COMPATIBILITY = {
    "A100": {"arch": "nvidia", "score": 10},
    "H100": {"arch": "nvidia", "score": 12},
    "RTX3090": {"arch": "nvidia", "score": 7},
    "MI300": {"arch": "amd", "score": 9},
    "GAUDI2": {"arch": "intel", "score": 8},
}

def get_gpu_score(gpu_type):
    return GPU_COMPATIBILITY.get(gpu_type, {}).get("score", 5)

def compatible(job_gpu, node_gpu):
    return GPU_COMPATIBILITY.get(node_gpu, {}).get("score", 0) >= \
           GPU_COMPATIBILITY.get(job_gpu, {}).get("score", 0)
