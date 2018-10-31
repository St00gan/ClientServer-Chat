import urllib.request
import os.path
with urllib.request.urlopen('http://ip.42.pl/raw') as response:
    html = response.read()
html = html.decode("utf-8")
print(str(html))
completeName = os.path.join("data","ip.txt")         
file1 = open(completeName, "w")
file1.write(html)
file1.close()
