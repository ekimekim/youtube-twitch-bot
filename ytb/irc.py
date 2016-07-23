
from girc import Client

from .config import CHANNEL, OAUTH, NICK
from .download import download

def run():
	client = Client(hostname='irc.chat.twitch.tv', nick=NICK, password=OAUTH, twitch=True)
	channel = client.channel(CHANNEL)
	channel.join()

	@client.handler(command='PRIVMSG', target=CHANNEL, payload=lambda s: s.startswith('!song '))
	def chat(client, message):
		cmd, url = message.payload.split(' ', 1)
		if not url:
			return
		try:
			title = download(url)
		except Exception as ex:
			channel.msg("Failed to download {!r}: {}".format(url, ex))
		else:
			channel.msg("Enqueued {}".format(title))

	client.start()
	client.wait_for_stop()
