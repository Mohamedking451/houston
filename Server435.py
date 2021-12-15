import requests
import time
headers = {"Authorization" : "OTIwNzQzMjAxNjY3NzA2ODkw.YbozHw.BlWXBitH4kx7gfi-HetCnR7gh1A"}
data1 = {"content" : "!d bump"}
while True:
	r = requests.post("https://discord.com/api/v9/channels/920546145623740426/messages", headers = headers, data = data1)
	print(r.status_code)
	time.sleep((60 * 60) * 2)
