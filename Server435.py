import requests
r = requests.post("https://discord.com/api/v9/channels/920546145623740426/messages", headers = {"Authorization" : "OTIwNjA3NDEwOTk2MDE1MTY0.Ybm3FQ.aPXLnbw1Z88jJhE8cHGnVepUML4"}, data = {"content" : "!d bump"})
print(r.json())

