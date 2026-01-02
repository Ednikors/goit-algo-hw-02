from queue import Queue
import random as rn
import time

request_counter = 0

def generate_request(queue):
    """
    Generates new requests and adds them to the queue.

    Parameters:
        queue: Queue object for storing requests

    Returns:
        None
    """
    global request_counter
    # random number of new requests (0-2)
    num_requests = rn.randint(0, 2)
    
    for _ in range(num_requests):
        request_counter += 1
        request_theme = rn.choice(['Consultation', 'Warranty', 'Repair'])
        request_priority = rn.choice(['Low', 'Medium', 'High'])
        
        request_data = {
            'number': request_counter,
            'theme': request_theme,
            'priority': request_priority
        }
        
        queue.put(request_data)
        print(f"Created request #{request_counter} | Type: {request_theme} | Priority: {request_priority}")
    
    if num_requests > 0:
        print("-" * 50)


def process_request(queue):
    """
    Processes a request from the queue.

    Parameters:
        queue: Queue object with requests

    Returns:
        None
    """
    if not queue.empty():
        request = queue.get()
        print(f"Processing request #{request['number']}")
        print(f"  Theme: {request['theme']}")
        print(f"  Priority: {request['priority']}")
        print("-" * 50)
    else:
        print("The queue is empty.")
        print("-" * 50)


def main():
    """
    Main function that runs the request processing simulation.
    Press Ctrl+C to exit the program.
    """
    request_queue = Queue()
    
    print("=" * 50)
    print("Service Center Request Processing System")
    print("Press Ctrl+C to exit")
    print("=" * 50)
    
    try:
        while True:
            # generate new requests
            generate_request(request_queue)
            
            # show queue status
            queue_size = request_queue.qsize()
            print(f"Requests in queue: {queue_size}")
            
            # process random number of requests (1-3)
            num_to_process = min(rn.randint(1, 3), queue_size)
            print(f"Processing {num_to_process} request(s)...")
            print("=" * 50)
            
            time.sleep(2)
            
            for _ in range(num_to_process):
                process_request(request_queue)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n" + "=" * 50)
        print("Program terminated. Goodbye!")
        print("=" * 50)


if __name__ == "__main__":
    main()



    