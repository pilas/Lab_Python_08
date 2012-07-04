import urllib
import urllib.request
import re
'''
# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://www.wunderground.com/global/stations/65432.html")
# Read from the object, storing the page's contents in 's'.
s = f.read()
f.close()


import webbrowser
webbrowser.open("http://www.wunderground.com/global/stations/65432.html")
f = urllib2.urlopen("http://www.wunderground.com/global/stations/65432.html")
s = f.read()
f.close()
.decode('utf8')  °C\s+'
'''
f = urllib.request.urlopen("http://www.wunderground.com/global/stations/65432.html")
s = f.read().decode('utf8')
f.close()

print( re.findall(r'(\d+(|\.)\d+)\&deg',s))
#print(s)


