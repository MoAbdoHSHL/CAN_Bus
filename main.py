from multiprocessing import Process, Queue
from can_listener import start_listener
from can_processor import start_processor
from kuksaval_publisher import start_publisher

if __name__ == "__main__":
    
    can_queue = Queue()
    processed_queue = Queue()

    
    listener_p = Process(target=start_listener, args=(can_queue,))
    processor_p = Process(target=start_processor, args=(can_queue, processed_queue))
    publisher_p = Process(target=start_publisher, args=(processed_queue,))

    listener_p.start()
    processor_p.start()
    publisher_p.start()

    listener_p.join()
    processor_p.join()
    publisher_p.join()