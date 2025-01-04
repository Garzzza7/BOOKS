from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import os

url = "https://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
pdfs = soup.find_all("a")
for pdf in pdfs:
    buf = str(pdf)
    buf = re.sub(r"<[^>]*>", "", buf)
    if ".pdf" in buf:
        urllib.request.urlretrieve(url + buf, buf)
        # os.system("wget " + url + buf)
        print(buf + " done")
