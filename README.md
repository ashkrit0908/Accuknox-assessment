# Accuknox Assessment - Django Signals & Custom Classes

This repository contains my solutions for the Accuknox Django Trainee assessment, covering Django Signals and Custom Classes in Python.

## 📋 Assessment Questions

### Topic: Django Signals

#### Question 1: Synchronous vs Asynchronous Execution
**Question**: By default are Django signals executed synchronously or asynchronously?

**Answer**: Django signals are executed **synchronously** by default.

**Proof**: See `question1_signals_sync_async.py` - The signal execution time (0.000005s) is less than the total time (0.000010s), proving signals execute before the `send()` method returns.

#### Question 2: Thread Execution
**Question**: Do Django signals run in the same thread as the caller?

**Answer**: Yes, Django signals run in the **same thread** as the caller.

**Proof**: See `question2_signals_threading.py` - Both caller and signal execute in the same thread ID (8361337024).

#### Question 3: Database Transaction Context
**Question**: By default do Django signals run in the same database transaction as the caller?

**Answer**: Yes, Django signals run in the **same database transaction** as the caller.

**Proof**: See `question3_signals_transaction.py` - Since signals are synchronous and run in the same thread, they inherit the same transaction context as the triggering operation.

### Topic: Custom Classes in Python

#### Question 4: Rectangle Class with Iteration
**Requirements**:
- Initialize with `length:int` and `width:int`
- Can be iterated over
- When iterated, yields `{'length': <VALUE>}` then `{'width': <VALUE>}`

**Implementation**: See `question4_rectangle_class.py`

**Features**:
- ✅ Type validation for length and width parameters
- ✅ Iterable using `for` loops
- ✅ Supports unpacking: `length_dict, width_dict = rect`
- ✅ Yields correct dictionary format
- ✅ Additional utility methods (area, perimeter)

## 🚀 Running the Code

Each question has its own separate file that can be run independently:

```bash
# Django Signals Tests
python3 question1_signals_sync_async.py
python3 question2_signals_threading.py
python3 question3_signals_transaction.py

# Rectangle Class Test
python3 question4_rectangle_class.py
```

## 📁 File Structure

```
├── question1_signals_sync_async.py      # Django signals sync/async test
├── question2_signals_threading.py       # Django signals threading test  
├── question3_signals_transaction.py     # Django signals transaction test
├── question4_rectangle_class.py         # Rectangle class implementation
└── README.md                           # This file
```

## 🧪 Test Results

### Django Signals
- **Synchronous Execution**: ✅ Proven with timing measurements
- **Same Thread**: ✅ Proven with thread ID comparison
- **Same Transaction**: ✅ Explained with transaction context inheritance

### Rectangle Class
- **Initialization**: ✅ Type validation working
- **Iteration**: ✅ Yields correct dictionary format
- **Unpacking**: ✅ Works with tuple unpacking
- **Multiple Iterations**: ✅ Can be iterated multiple times

## 💡 Key Insights

1. **Django Signals are Synchronous**: They execute immediately when triggered, blocking the calling code until completion.

2. **Thread Safety**: Since signals run in the same thread, they're not inherently thread-safe and should be used carefully in multi-threaded environments.

3. **Transaction Context**: Signals inherit the database transaction context, meaning exceptions in signal handlers can cause transaction rollbacks.

4. **Python Iteration**: The `__iter__()` method as a generator function allows for clean, reusable iteration over custom objects.

## 👨‍💻 Author

**Ashkrit Shukla** - Django Developer with 3 years of experience

---

*This assessment demonstrates understanding of Django signals behavior and Python custom class implementation with iteration protocols.*
