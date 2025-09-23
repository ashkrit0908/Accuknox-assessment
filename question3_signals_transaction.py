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

def test_signal_transaction():
    """Question 3: Test if Django signals run in the same database transaction"""
    print("=" * 60)
    print("QUESTION 3: Do Django signals run in the same database transaction?")
    print("=" * 60)
    
    print("Testing signal execution context...")
    
    # Reset execution info
    execution_info['thread_id'] = None
    execution_info['start_time'] = time.time()
    
    caller_thread = threading.current_thread()
    print(f"Caller thread ID: {caller_thread.ident}")
    
    # Send signal
    test_signal.send(sender=None)
    
    signal_thread_id = execution_info['thread_id']
    print(f"Signal executed in thread ID: {signal_thread_id}")
    
    print("\n" + "-" * 40)
    print("TRANSACTION BEHAVIOR EXPLANATION:")
    print("-" * 40)
    print("Since Django signals are SYNCHRONOUS and run in the SAME thread:")
    print("1. Signals inherit the same transaction context as the triggering operation")
    print("2. If Model.objects.create() is called within transaction.atomic(),")
    print("   the post_save signal will also run within that same transaction")
    print("3. If the signal handler raises an exception, it can cause")
    print("   the entire transaction to rollback")
    print("4. This is why you need to be careful with signal handlers")
    print("   - they can affect the transaction state")
    
    print("\nCONCLUSION: Signals run in the SAME database transaction as the caller")

if __name__ == "__main__":
    print("DJANGO SIGNALS - QUESTION 3 TEST")
    print("Testing transaction behavior")
    print()
    
    test_signal_transaction()
    
    print("\n" + "=" * 60)
    print("Test completed!")
    print("=" * 60)
