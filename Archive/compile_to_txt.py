import os

index = os.listdir("/Users/patrickeells/PycharmProjects/1q84/search_match/") # returns list
print(index)

def read_input_file(path):
        f = open(path)
        content = f.readlines()
        f.close()
        return content

content = []
for title in index:
    if title == '.DS_Store':
        continue
    line = read_input_file("search_match/{0}".format(title))
    content.append(line)
    #print(content) - check if i got the info

outfile_name = "search_match/compiled.txt"
outfile = open(outfile_name, "w")
for line in content:
    outfile.writelines(line)
outfile.close()