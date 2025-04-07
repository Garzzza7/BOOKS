import os


def process_url(url, cnt):
    url1 = ""
    url2 = ""
    name = ""
    smallname = ""
    if cnt >= 0 and cnt <= 9:
        url1 = url + "0" + str(cnt) + "/" + "Slides0" + str(cnt) + ".pdf"
        url2 = url + "0" + str(cnt) + "/" + "Small0" + str(cnt) + ".pdf"
        name = "Slides0" + str(cnt) + ".pdf"
        smallname = "Small0" + str(cnt) + ".pdf"
    else:
        url1 = url + str(cnt) + "/" + "Slides" + str(cnt) + ".pdf"
        url2 = url + str(cnt) + "/" + "Small" + str(cnt) + ".pdf"
        name = "Slides" + str(cnt) + ".pdf"
        smallname = "Small" + str(cnt) + ".pdf"
    print(url1)
    print(url2)
    os.system("wget " + url1)
    os.system("wget " + url2)
    os.system("mkdir " + str(cnt))
    os.system("mv " + name + " " + str(cnt))
    os.system("mv " + smallname + " " + str(cnt))


url = "https://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/"
for i in range(0, 19):
    process_url(url, i)
print("ALL DONE!!!!!")
