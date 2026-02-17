kv_cache_registry = {}

def store_cache(model, key, location):
    kv_cache_registry[(model, key)] = location

def lookup_cache(model, key):
    return kv_cache_registry.get((model, key))
