
import os
import re

from gevent.lock import RLock

from easycmd import cmd

OUTPUT_TEMPLATE = '%(autonumber)s-%(title)s-%(id)s.%(ext)s'

lock = RLock()

def download(url):
	from main import session_folder
	with lock:
		filename = cmd(['youtube-dl', '--no-playlist', '-o', OUTPUT_TEMPLATE, '--get-filename', url]).strip()
		filename, ext = os.path.splitext(filename)
		filename = re.sub('[^A-Za-z0-9.-_]', '_', filename)
		filepath = '{}.%(ext)s'.format(filename)
		output_path = os.path.join(session_folder, filepath)
		cmd(['youtube-dl', '--no-playlist', '-o', output_path, '-x', '--audio-format=mp3', url])
	return filename
