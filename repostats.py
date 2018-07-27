import csv, os

regex ="anzsrc"
datadir = "data/"
headersearchtext ="marsden"
outputfile = "subjects.txt"


f = open(outputfile, "+a", encoding="utf8") 

for filename in os.listdir(path=datadir):

    with open(datadir+filename, 'r', newline='', encoding="utf8", ) as csvfile:
        records = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        headers = next(reader)
        print(headers)
        subjectposition = [i for i, s in enumerate(headers) if headersearchtext in s]
        print(subjectposition)
        for row in records:
            for i in subjectposition:
                if len(row[i]) > 0: 
                    subjects= row[i].split("||")
                    print(subjects)
                    for j in subjects:
                        f.write(j+"\n")
f.close()     