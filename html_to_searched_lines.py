import os
from bs4 import BeautifulSoup
import re

def read_input_file(path):
    f = open(path)
    content = f.read()
    f.close()
    return content

def read_input_filelines(path):
    f = open(path)
    content = f.readlines()
    f.close()
    return content

def html_parser_p(index_list):
    '''takes an index of a directory and parses all of the <p>'s and writes
    them to a directory called 'html_parsed' '''
    for title in index_list:
        content = read_input_file(str("html_index/{0}".format(title)))
        #print(content) - check if i got the info
        soup = BeautifulSoup(content, "html.parser")
        outfile_name = "html_parsed/{0}".format(title)
        outfile = open(outfile_name, "w") #TODO - put them in the same line?
        all_p = soup.find_all("p")
        data = []
        for p in all_p:
            data.append(p)
        outfile.write(str(data))
        outfile.close()
    return

def html_to_text(index_list):
    for title in index_list:
        content = read_input_file(str("html_parsed/{0}".format(title))) #TODO - pull out the str
        #print(content) - check if i got the info

        soup = BeautifulSoup(content, "html.parser")

        outfile_name = "txt_files/{0}.txt".format(title)
        outfile = open(outfile_name, "w")
        all_p = soup.get_text()
        all_p = all_p.replace('., ', '.\n')
        all_p = all_p.replace('. ', '.\n')
        outfile.writelines(all_p)
        outfile.close()
    return

def search_for_food(index_list):
    foods = read_input_filelines("food.txt")
    foods = list(map(str.strip,foods))
    #print(foods)
    for title in index_list:
        content = read_input_filelines(str("txt_files/{0}".format(title)))
        #print(content) - check if i got the info
        outfile_name = "search_match/matched{0}".format(title)
        outfile = open(outfile_name, "w")
        for food in foods:
            for line in content:
                if food in line:#todo - if line already exists don't add it
                    outfile.write(line)
        outfile.close()
        if os.path.getsize(outfile_name)==0:
            os.remove(outfile_name)
    return

def compile_text(index_list):#TODO - something goofy here - priority #1
    content = []
    for title in index_list:
        if title == '.DS_Store':
            continue
        line = read_input_filelines("search_match/{0}".format(title))
        content.append(line)
    #print(content)# - check if i got the info
    outfile_name = "compiled.txt"
    outfile = open(outfile_name, "w")
    i=0
    for line in content:
        for row in line:
            outfile.writelines('{0:>4} {1:>6} {2}'.format(i, len(row), row))
            #outfile.writelines(line)
            i+=1
    outfile.close()
    return

def scrub_dir():
    for title in os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_parsed/"):
        os.remove('html_parsed/{0}'.format(title))
    for title in os.listdir("/Users/patrickeells/PycharmProjects/1q84/txt_files/"):
        os.remove('txt_files/{0}'.format(title))
    for title in os.listdir("/Users/patrickeells/PycharmProjects/1q84/search_match/"):
        os.remove('search_match/{0}'.format(title))
    if os._exists('compiled.txt')==True:
        os.remove('complied.txt')
    return

scrub_dir()
#html_index_list = os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_index/") # returns list of html files in html_index/
#print(os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_index/"))
html_parser_p(os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_index/")) #parses for all <p>'s and puts them in html files in /html_parsed/

#html_parsed_list = os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_parsed/") #returns list of html files in html_parsed/
html_to_text(os.listdir("/Users/patrickeells/PycharmProjects/1q84/html_parsed/")) #puts sentences on individual lines

search_for_food(os.listdir("/Users/patrickeells/PycharmProjects/1q84/txt_files/"))#searches for items in food.txt
compile_text(os.listdir("/Users/patrickeells/PycharmProjects/1q84/search_match/"))