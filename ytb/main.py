
import time
import os

import gevent

from . import app
from . import irc
from .config import STATIC_FOLDER

songs = []
session = time.strftime('%F-%H-%M-%S')

session_folder = os.path.join(STATIC_FOLDER, session)
if not os.path.exists(session_folder):
	os.mkdir(session_folder)

def main(*args):
	g_app = gevent.spawn(app.run)
	g_irc = gevent.spawn(irc.run)
	try:
		ready = gevent.wait([g_app, g_irc], count=1)
		for g in ready:
			g.get() # let it raise
	finally:
		gevent.killall([g_app, g_irc], block=True)
