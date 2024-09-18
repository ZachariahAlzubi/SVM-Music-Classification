
# utils.py

from datetime import datetime

def start_timer():
    """Starts a timer for tracking performance."""
    return datetime.now()

def end_timer(start_time):
    """Ends the timer and prints the elapsed time."""
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time}")
