queue = []

def add_job(job):
    queue.append(job)

def get_job():
    if queue:
        return queue.pop(0)
    return None
