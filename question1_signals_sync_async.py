import time
from django.dispatch import Signal
from django.dispatch import receiver

# Create a custom signal for testing
test_signal = Signal()

# Global variables to track execution
execution_info = {
    'execution_time': None,
    'start_time': None,
    'end_time': None
}

@receiver(test_signal)
def signal_handler(sender, **kwargs):
    """Signal handler to capture execution details"""
    execution_info['end_time'] = time.time()
    execution_info['execution_time'] = execution_info['end_time'] - execution_info['start_time']
    
    print(f"Signal executed!")
    print(f"Signal execution time: {execution_info['execution_time']:.6f} seconds")

def test_signal_sync_async():
    # Reset execution info
    execution_info['start_time'] = time.time()
    
    print("Sending signal...")
    start_time = time.time()
    
    # Send the signal
    test_signal.send(sender=None)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"Signal send completed in: {total_time:.6f} seconds")
    print(f"Signal execution time: {execution_info['execution_time']:.6f} seconds")
    
    if execution_info['execution_time'] < total_time:
        print("CONCLUSION: Signals are SYNCHRONOUS - they execute before send() returns")
    else:
        print("CONCLUSION: Signals are ASYNCHRONOUS - they execute after send() returns")

if __name__ == "__main__":
    print("Testing synchronous vs asynchronous execution")

    test_signal_sync_async()
    
