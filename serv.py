from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello'

@app.route('/test', methods = ['POST'])
def test():
	return request.form['hello']

if __name__ == '__main__':
	app.run(debug=True)
