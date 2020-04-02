s = "def http://alegeaa.com is where to go <here is me>"

openb_pos = s.find("<")
closeb_pos = s.find(">", openb_pos)


string = s[openb_pos + 1:closeb_pos]
print(string)
