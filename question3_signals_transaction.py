import threading
import time
from django.dispatch import Signal
from django.dispatch import receiver

# Create a custom signal for testing
test_signal = Signal()

# Global variables to track execution
execution_info = {
    'thread_id': None,
    'start_time': None,
    'in_transaction': False
}

@receiver(test_signal)
def signal_handler(sender, **kwargs):
    """Signal handler to capture execution details"""
    current_thread = threading.current_thread()
    execution_info['thread_id'] = current_thread.ident
    
    print(f"Signal executed in thread: {current_thread.ident}")
    print("Note: For full transaction testing, we need Django models and database setup")

