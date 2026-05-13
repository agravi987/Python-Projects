from flask import Flask, render_template
import psutil # for system monitoring
import platform # for getting system information
import socket # for getting hostname and IP address
import datetime # for getting current time



app = Flask(__name__)


@app.route('/')
def home():

    cpu_percent = psutil.cpu_percent(interval=1) 

    memory = psutil.virtual_memory() 

    disk = psutil.disk_usage('/')

    boot_time = datetime.datetime.fromtimestamp(
        psutil.boot_time()
    )

    system_info = {
        "hostname" : socket.gethostname(),
        "system" : platform.system(),
        "release" : platform.release(),
        "cpu_usage" : cpu_percent,
        "memory_usage" : memory.percent,
        "disk_usage" : disk.percent, 
        "boot_time" : boot_time.strftime("%Y-%m-%d %H:%M:%S")
    }


    return render_template('index.html',info=system_info)

if __name__ == '__main__':
    app.run(debug=True)