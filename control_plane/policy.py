def enforce_policy(job, node):
    if job.get("region_required") and job["region_required"] != node["location"]:
        return False

    if job.get("carbon_sensitive") and node.get("carbon_score", 50) > 30:
        return False

    if job.get("compliance") == "strict" and node["location"] != "India":
        return False

    return True
