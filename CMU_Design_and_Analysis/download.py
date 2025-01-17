from bs4 import BeautifulSoup
import urllib.request
import requests
import re

url = "https://www.cs.cmu.edu/~15451-f23/lectures/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
pdfs = soup.find_all("a")
for pdf in pdfs:
    buf = str(pdf)
    buf = re.sub(r"<[^>]*>", "", buf)
    if ".pdf" in buf:
        urllib.request.urlretrieve(url + buf, buf)
        print(buf + " done")
print("ALL DONE!!!!!")
