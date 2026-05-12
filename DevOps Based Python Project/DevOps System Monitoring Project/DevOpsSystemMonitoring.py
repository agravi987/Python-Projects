"""
Your Python app will:

Show CPU usage
Show RAM usage
Show Disk usage
Show Running Processes
Save logs to a file
Alert when CPU is high
Run continuously like a monitoring agent

Basically like a mini DevOps monitoring tool

"""

import psutil # For system monitoring
import time     # For sleep intervals
import logging # For logging system metrics and alerts

# Set up logging configuration
logging.basicConfig(
    filename='system_monitor.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
) 

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent


    log_message = f"CPU: {cpu}% | Memory: {ram}% | Disk: {disk}%"

    
    if cpu > 80:
        logging.warning("ALERT: CPU usage is high!")
    else:
        logging.info(log_message)

    print(log_message)


    time.sleep(5)  # Wait for 5 seconds before the next check   