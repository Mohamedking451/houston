import requests
import time
while True:
	r = requests.post("https://discord.com/api/v9/channels/920546145623740426/messages", headers = {"Authorization" : "OTE4NDA2MzA1NDExMTI5MzY0.Ybm48Q.6TnInPz7f6UdecKv2WHhjPbYehs"}, data = {"content" : "!d bum"})
	print(r.json())
	time.sleep((60 * 60) * 2)


