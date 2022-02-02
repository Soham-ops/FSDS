import time
from datetime import datetime
def print_time1(timer):
    
    print(f"I will wait for {timer} secs")
    time.sleep(timer)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    
def print_time2(timer):
    
    print(f"I will wait for {timer} secs")
    time.sleep(timer)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    
    
def print_time3(timer):
    
    print(f"I will wait for {timer} secs")
    time.sleep(timer)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)