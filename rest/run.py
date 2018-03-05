from eve import Eve
import platform
import psutil
import flask
from flask import jsonify

app = Eve()


@app.route('/processor',methods=['GET'])
def processor():
    processordata = {
       "ProcessorName": platform.processor(),
       "System Name": platform.system(),
       "Version": platform.version(),
       "Node": platform.node(),
       "Release": platform.release()
    }
    return send_response(processordata)

@app.route('/disk',methods=['GET'])
def disk():
    disk_usage = psutil.disk_usage('/')
    diskdata = {
       "Total Disk Size": disk_usage.total,
       "Disk Free": disk_usage.free,
       "Disk Used": disk_usage.used
    }
    return send_response(diskdata)

@app.route('/ram',methods=['GET'])
def ram():
    ramdata = {
       "Total Ram": psutil.virtual_memory().total,
       "Ram Free": psutil.virtual_memory().available,
       "Ram Used": psutil.virtual_memory().used
    }
    return send_response(ramdata)

def send_response(data):
    return flask.jsonify(**data)

if __name__ == '__main__':
    app.run()
