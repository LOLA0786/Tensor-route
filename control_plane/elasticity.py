elasticity_signals = {
    "bid_prices": [],
    "clearing_prices": [],
    "job_acceptance_rate": [],
}

def record_bid(price):
    elasticity_signals["bid_prices"].append(price)

def record_clearing(price):
    elasticity_signals["clearing_prices"].append(price)

def record_acceptance(accepted):
    elasticity_signals["job_acceptance_rate"].append(accepted)
