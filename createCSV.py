import csv


def createTwoCSV(retdict):
    createdomName(retdict)


def createdomName(retdict):
    with open('domName.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)

        id_url = 0
        for i in retdict:
            # print(([id_url, i, retdict[i]]))
            filewriter.writerow([id_url, i, retdict[i]])
            id_url += 1



def createdomAdjacence(retdict):
    pass
