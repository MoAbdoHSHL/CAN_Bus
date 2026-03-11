from kuksa_client.grpc import VSSClient
from multiprocessing import Queue

def start_publisher(processed_queue):
    client = VSSClient("localhost", 55555)
    print("Publisher: Connecting to KUKSA Databroker on localhost:55555...")
    with client:
        while True:
            data = processed_queue.get()
            path = data["name"]
            value = data["value"]
            client.set_current_values({path: value})
            print(f"Publisher: Sent {path} = {value}")