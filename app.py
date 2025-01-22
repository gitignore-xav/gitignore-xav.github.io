from flask import Flask, redirect, url_for, render_template
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('index.html')

if __name__ == "__main__":
	# app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
	from waitress import serve
	serve(app, host="127.0.0.1", port=8080, url_scheme='https')
