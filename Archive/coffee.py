import os
from bs4 import BeautifulSoup

html_index = os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_index/") # returns list
def read_input_file(path):
        f = open(path)
        content = f.read()
        f.close()
        return content

for title in html_index:
    content = read_input_file(str("html_index/{0}".format(title)))
    #print(content) - check if i got the info

    soup = BeautifulSoup(content, "html.parser")

    outfile_name = "html_parsed/{0}".format(title)
    outfile = open(outfile_name, "w")
    all_p = soup.find_all("p", class_="calibre34")

    data = []
    for p in all_p:
        data.append(p)
    outfile.write(str(data))
    outfile.close()