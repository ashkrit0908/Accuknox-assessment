import threading
from django.dispatch import Signal
from django.dispatch import receiver

# Create a custom signal for testing
test_signal = Signal()

# Global variable to track thread ID
signal_thread_id = None

@receiver(test_signal)
def signal_handler(sender, **kwargs):
    """Signal handler to capture thread ID"""
    global signal_thread_id
    signal_thread_id = threading.current_thread().ident

def test_signal_transaction():
    """Test if signals run in the same thread as caller"""
    global signal_thread_id
    
    # Get caller thread ID
    caller_thread_id = threading.current_thread().ident
    print(f"Caller thread ID: {caller_thread_id}")
    
    # Send signal
    test_signal.send(sender=None)
    
    print(f"Signal executed in thread ID: {signal_thread_id}")
    
    # Compare thread IDs
    if caller_thread_id == signal_thread_id:
        print("CONCLUSION: Signals run in the SAME thread as the caller")
    else:
        print("CONCLUSION: Signals run in a DIFFERENT thread from the caller")

if __name__ == "__main__":
    print("Testing thread execution behavior")
    test_signal_transaction()

