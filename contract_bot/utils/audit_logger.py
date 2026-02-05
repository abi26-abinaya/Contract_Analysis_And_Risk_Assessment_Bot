import json
from datetime import datetime

def save_audit(data):

    filename = f"audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
