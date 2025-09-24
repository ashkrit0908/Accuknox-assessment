import threading
import time
from django.dispatch import Signal
from django.dispatch import receiver

# Create a custom signal for testing
test_signal = Signal()

# Global variables to track execution
execution_info = {
    'thread_id': None,
    'start_time': None
}

@receiver(test_signal)
def signal_handler(sender, **kwargs):
    """Signal handler to capture execution details"""
    current_thread = threading.current_thread()
    execution_info['thread_id'] = current_thread.ident
    
    print(f"Signal executed in thread: {current_thread.ident}")

def test_signal_threading():
    # Reset execution info
    execution_info['thread_id'] = None
    execution_info['start_time'] = time.time()
    
    caller_thread = threading.current_thread()
    print(f"Caller thread ID: {caller_thread.ident}")
    
    # Send signal
    test_signal.send(sender=None)
    
    signal_thread_id = execution_info['thread_id']
    print(f"Signal executed in thread ID: {signal_thread_id}")
    
    if caller_thread.ident == signal_thread_id:
        print("CONCLUSION: Signals run in the SAME thread as the caller")
    else:
        print("CONCLUSION: Signals run in a DIFFERENT thread from the caller")

if __name__ == "__main__":
    print("Testing thread execution behavior")
    test_signal_threading()
    
    print("Test completed!")

