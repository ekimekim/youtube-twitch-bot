
import os

from flask import Flask

from config import STATIC_FOLDER

app = Flask(
	__name__,
	static_url_path='/static',
	static_folder=STATIC_FOLDER,
)

@app.route('/')
def listsongs():
	return '\n'.join(get_filenames())

def get_filenames():
	from main import session, session_folder
	return ['{}/{}'.format(session, song) for song in os.listdir(session_folder)]

def run(debug=False):
	host = '127.0.0.1' if debug else '0.0.0.0'
	app.run(host=host, port=8000, debug=debug)
