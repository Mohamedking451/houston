import requests
import time
while True:
	r = requests.post("https://discord.com/api/v9/channels/920546145623740426/messages", headers = {"Authorization" : "OTE4NDA2MzA1NDExMTI5MzY0.Ybm6hA.ywbmSW3UVmr_uS-Ium8ZelLt1n0"}, data = {"content" : "!d bump"})
	print(r.json())
	time.sleep((60 * 60) * 2)


