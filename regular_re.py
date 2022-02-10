import urllib.request
import re
url="https://www.summet.com/dmsi/html/codesamples/addresses.html"
action=urllib.request.urlopen(url)
html=action.read()
html_sta=html.decode()
print(re.findall(r'<li>([A-Z][a-z]+)',html_sta))
print("names...................")
print(re.findall(r'<li>([A-Z][a-z]+\s[A-Z][a-z]+)',html_sta))