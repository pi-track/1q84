import os
from bs4 import BeautifulSoup
import re

index = os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_parsed/") # returns list
def read_input_file(path):
        f = open(path)
        content = f.read()
        f.close()
        return content

for title in index:

    content = read_input_file(str("html_parsed/{0}".format(title)))
    #print(content) - check if i got the info

    soup = BeautifulSoup(content, "html.parser")

    outfile_name = "txt_files/{0}.txt".format(title)
    outfile = open(outfile_name, "w")
    all_p = soup.get_text()
    all_p = all_p.replace('. ', '\n')
    outfile.writelines(all_p)
    outfile.close()