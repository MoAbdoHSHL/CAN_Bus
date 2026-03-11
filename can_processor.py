from can_listener import Queue  
from multiprocessing import Queue

#CSV IDs
CAN_DECODING = {
    0x009: {"name": "target_speed", "bytes": (0,1), "order": "little", "type": "uint16", "scale": 0.1},
    0x06A: {"name": "precise_speed", "bytes": (0,3), "order": "big", "type": "uint32", "scale": 0.01},
    0x065: {"name": "vehicle_speed", "bytes": (0,1), "order": "big", "type": "uint16", "scale": 1.0},
    0x066: {"name": "cumulative_distance", "bytes": (0,3), "order": "big", "type": "uint32", "scale": 1.0},
    0x06B: {"name": "raw_wheel_RPM", "bytes": (0,1), "order": "big", "type": "uint16", "scale": 1.0},
    0x188: {"name": "wheel_freq", "bytes": (0,1), "order": "little", "type": "uint16", "scale": 1.0},
    0x067: {"name": "SOC", "bytes": (0,1), "order": "big", "type": "uint16", "scale": 1.0},
    0x068: {"name": "cumulative_voltage", "bytes": (0,3), "order": "big", "type": "uint32", "scale": 0.1},
    0x069: {"name": "current", "bytes": (0,3), "order": "big", "type": "uint32", "scale": 0.1},
}

def decode_can_message(msg):
    if msg.arbitration_id not in CAN_DECODING:
        return None

    rule = CAN_DECODING[msg.arbitration_id]
    start, end = rule["bytes"]
    raw_bytes = msg.data[start:end+1]

    if rule["type"] == "uint16":
        value = int.from_bytes(raw_bytes, byteorder=rule["order"])
    elif rule["type"] == "uint32":
        value = int.from_bytes(raw_bytes, byteorder=rule["order"])
    else:
        return None

    value *= rule.get("scale", 1)
    return {"name": rule["name"], "value": value}

def start_processor(can_queue, processed_queue):
    print("Processor: Waiting for CAN messages...")
    while True:
        msg = can_queue.get()
        decoded = decode_can_message(msg)
        if decoded:
            print(f"Processor: Decoded {decoded['name']} = {decoded['value']}")
            processed_queue.put(decoded)