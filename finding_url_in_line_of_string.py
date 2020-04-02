s = "def http://alegeaa.com is where to go"

http_pos = s.find("http://")
space_pos = s.find(" ", http_pos)


url = s[http_pos:space_pos]
print(url)
