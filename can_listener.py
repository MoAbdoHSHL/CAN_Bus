import can
from multiprocessing import Queue


def start_listener(can_queue):
    INTERESTED_IDS = [
        0x009, 0x06A, 0x065, 0x066, 0x06B, 0x188,
        0x067, 0x068, 0x069
    ]

    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print("Listener: Listening on vcan0...")

    while True:
        msg = bus.recv()
        if msg and msg.arbitration_id in INTERESTED_IDS:
            print(f"Listener: RX {hex(msg.arbitration_id)} {msg.data.hex()}")
            can_queue.put(msg)