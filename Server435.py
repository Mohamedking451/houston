import requests
re = requests.post("https://discord.com/api/v9/auth/login", json = {"email" : "lmoa62626@gmail.com", "password" : "deeq1012"})
r = requests.post("https://discord.com/api/v9/channels/920546145623740426/messages", headers = {"Authorization" : re.json()["token"]}, data = {"content" : "!d bump"})
print(r.json())

