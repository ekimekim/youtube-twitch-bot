
import os

STATIC_FOLDER = '/tmp/ytb'
NICK = 'ekimekim3000'
CHANNEL = '#ekimekim3000'
OAUTH_PATH = '/home/mike/.twitch-irc.oauth'

if not os.path.exists(STATIC_FOLDER):
	os.mkdir(STATIC_FOLDER)

with open(OAUTH_PATH) as f:
	OAUTH = f.read().strip()
