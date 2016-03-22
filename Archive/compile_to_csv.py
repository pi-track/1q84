import os
import csv

index = os.listdir("/Users/patrickeells/PycharmProjects/1q84/search_match/") # returns list

def read_input_file(path):
    content =[]
    for line in open(path):
        content.append(line)
    return content

#for title in index:
    #content = read_input_file(str("search_match/{0}".format(title)))
content = read_input_file(str("search_match/13.txt"))
print(content)# - check if i got the info


with open('lines.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(len(content)):
        writer.writerow(content[i])
