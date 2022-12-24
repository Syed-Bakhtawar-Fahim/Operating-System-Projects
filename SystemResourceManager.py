# Simple Command line tool to show you real time CPU usage and memeory usage of the system
# pip install psutil --> for getting the data
import time
import psutil

# We want to define a funtion which will visualize those value
def display_usage(cpu_usage, mem_usage, bars = 50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = "||" * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = "||" * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    # Print the data
    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage: .2f}% ", end = "" )
    print(f"\MEM Usage: |{mem_bar}| {mem_usage: .2f}% ", end = "\r" )


while True: 
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(.5)