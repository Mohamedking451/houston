import requests
re = requests.post("https://discord.com/api/v9/auth/login", json = {"email" : "helly657@gmail.com", "password" : "deeq1012"})
r = requests.post("https://discord.com/api/v9/channels/920546145623740426/messages", headers = {"Authorization" : "OTE4NTMwNTk5NDMyNjQ2Njk2.YbmxuA._GdBmXcPE5g1xq5Al26JL2KHKw0"}, data = {"content" : "!d bump"})
print(re.json())
print(r.json())
