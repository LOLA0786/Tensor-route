from control_plane.metrics import system_metrics

def scaling_signal():
    load = system_metrics["active_jobs"]

    if load > 5:
        return "scale_up"
    if load == 0:
        return "scale_down"
    return "stable"
