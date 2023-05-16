# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import gzip
import copy
#import logging

#logging.basicConfig(filename="x12.log", level=logging.DEBUG)

header = ['ELEMENT', 'INSURED', 'PERSON', 'LASTNAME', 'FIRSTNAME', 'MIDDLENAME', 'PREFIX', 'SUFFIX', 'QUALIFIER', 'SSN'] #erik

_2000 = {
    "INS" : "MemberLevelDetail",
    "REF" : "SubscriberIdentifier"
}

_2100A = {
    "NM1" : "MemberName",
    "PER" : "MemberCommmunicationsNumbers",
    "N3"  : "MemberResidenceStreetAddress",
    "N4"  : "MemberCityStateZipCode",
    "DMG" : "MemberDemographics"
}

_2300 = {
    "HD"  : "HealthCoverage",
    "DTP" : "HealthCoverageDates",
    "REF" : "HealthCoveragePolicyNumber"
}

_834 = [_2000, _2100A, _2300]

def func(filename):
    lista = []
    maxcol = 0

    with gzip.open(filename, 'rb') as f:
        file_content = f.readline()
        file_content = str(file_content).split("~")

    for i in file_content:
        lista.append(i.split("*"))
        if len(lista[-1]) > maxcol:
            maxcol = len(lista[-1])

    del(lista[len(lista)-1])

    lista[0][0] = 'NM1'

    newlista = copy.deepcopy(lista)

    i = 0
    j = 0

    loop = 0

    for k in newlista:
        j = 0
        for l in newlista[i]:
            if l == '':
                l = ' '
            if j == 0:
                if l == 'INS':
                    loop = 0
                if l == 'NM1':
                    loop += 1
                elif l == 'HD':
                    loop += 1
                if l in _834[loop].keys():
                    newlista[i][j] = _834[loop][l]
                else:
                    newlista[i][j] = l
            else:
                newlista[i][j] = l
            j+=1
            loop = 0
        i+=1

    heading = []#erik

    for x in range(maxcol):#erik
        heading.append(header[x]) #erik

    myList = [] #erik
    myList.append(heading) #erik

    for h in newlista:
        myList.append(h) #erik

    return myList, maxcol

#    return newlista[2], maxcol

