import psutil
from flask import Flask

app = Flask(__name__)
#app created with parameter names as __name__

#set path for home path
@app.route('/')
def index():
    cpu_percent = psutil.cpu_percent() #Get CPU usage percentage
    mem_percent = psutil.virtual_memory().percent #Get Memory usage percentage
    Message = None #Initialize Message variable
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory usage detected! Please scale up your resources."
    return f"CPU Usage: {cpu_percent}%, Memory Usage: {mem_percent}%. {Message}" #Return CPU and Memory usage with message if any

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    