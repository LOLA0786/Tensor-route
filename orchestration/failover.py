from control_plane.logger import log

def retry(job):
    log(f"Retrying job {job['id']}")
