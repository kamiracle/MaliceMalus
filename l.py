from flask import Flask
from flask import request
from werkzeug import secure_filename
import time
import sqlite3


app = Flask(__name__)

@app.route('/')
def hello_world():
    	return 'Hello World! hot edit'

@app.route('/data', methods=['POST'])
def post_data():

	for file in request.files:
		t = time.strftime("%b_%d_%Y_%H-%M-%S")
		f = request.files[file]
		f.save(secure_filename(f.filename) + "_" + t) 
	return 'Post'

@app.route('/cnc', methods=['GET'])
def cnc():

	uid = request.args.get('uid')
	command = 2
	
	if (uid != None):
		try:
			conn = sqlite3.connect('call_back.db')
			c = conn.cursor()
			c.execute('INSERT INTO callbacks(uid, rx_data, dtg) VALUES (?,?,?)', (str(uid), str(command), int(time.mktime(time.gmtime()))))
			conn.commit()

		except Exception, e:
			print str(e)

	print request.args.get('uid')
	return str(command)

if __name__ == '__main__':
    	app.debug = True
	app.run(host='0.0.0.0', port=5001)

