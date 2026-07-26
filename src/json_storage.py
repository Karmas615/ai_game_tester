import json
import os

def save_results(data, path="results.json"):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                old = json.load(f)
        except:
            old = []
    else:
        old = []

    old.append(data)

    with open(path, "w") as f:
        json.dump(old, f, indent=4)
