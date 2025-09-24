import threading
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
