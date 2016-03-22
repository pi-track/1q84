import os
from bs4 import BeautifulSoup

index = os.listdir("/Users/patrickeells/PycharmProjects/1q84/txt_files/") # returns list

def read_input_file(path):
        f = open(path)
        content = f.readlines()
        f.close()
        return content

i=0
for title in index:
    content = read_input_file(str("txt_files/{0}".format(title)))
    foods = read_input_file("food.txt")
    #print(content) - check if i got the info


    outfile_name = "search_match/{0}.txt".format(i)
    outfile = open(outfile_name, "w")
    for line in content:
        for food in foods:
            if food in line:
                outfile.writelines(line)
    outfile.close()
    if os.path.getsize(outfile_name)==0:
        os.remove(outfile_name)
    i+=1