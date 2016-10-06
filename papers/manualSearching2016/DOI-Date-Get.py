# Code by Matt Mayernik, mayernik@ucar.edu
# Written in Python 3.3
# This script takes in a list of DOIs, and returns a file of DOIs + dates of publication for those DOIs

import urllib
from urllib.request import Request, urlopen
from urllib.error import  URLError
import re

file_name = 'INSERT FILE NAME HERE'      #CHANGE THIS VALUE TO THE APPROPRIATE FILE

file = open(file_name + '.txt').readlines()

# the output of this script is a file named FILENAME_out.txt, where FILENAME is the same as the original input filename
output = open(file_name + '_out.txt', "w")

# remove any extra returns in the data file
c = 0
c = file.count("\n")
if c != 0:
    while c > 0:
        file.remove("\n")
        c = c - 1

# the fail list is used below to compile the DOIs that do not resolve, i.e. no metadata is returned
fail = []

for line in file:
    cleanDOI = str(line)
    cleanDOI = re.sub("\n", "", cleanDOI)
    url = "http://dx.doi.org/" + cleanDOI
    #url = "http://dx.doi.org/10.1126/science.1197869"
    #url = "http://dx.doi.org/10.1175/2010JHM1297.1"        #NARCCAP article
    #url = "http://dx.doi.org/10.5065/D6WD3XH5"          #NCL DOI
    #url = "http://dx.doi.org/10.5065/D6RN35ST"             #NARCCAP DOI
    headers = {"Accept": "text/turtle"}
    #headers = {"Accept": "Application/x-datacite+xml"}
    values = {"-D": "-", "-L": ""}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data, headers)
    try:
        response = urlopen(req)
        metadata = response.read()
        #print(metadata)

        #converts the response from 'bytes' to a string
        m = str(metadata, 'utf-8')

        #finds all lines that have these terms in them
        '''
        print(url + "\n AUTHOR")
        print(re.findall(".+http://xmlns.com/foaf/0.1/name.+",m))
        print("\nTITLE")
        print(re.findall(".+title.+",m))
        print("\nVOLUME")
        print(re.findall(".+volume.+",m))
        print("\nISSUE")
        print(re.findall(".+issue+",m))
        print("\nDATE")
        print(re.findall(".+date.+",m))
        print("\nPAGE")
        print(re.findall(".+page.+",m))
        '''
        
        # Find the date string by finding it in the returned XML
        #Y_string = re.findall(".+http://www.w3.org/2001/XMLSchema#gYearMonth.+",m)
        Year_string = re.findall(".+http://www.w3.org/2001/XMLSchema#.+",m)
        Year = re.split("\"",Year_string[0]) #Needs to be a string

        # print the URL and date in the console so that you can see the script proceeding through the DOI list
        print(url)
        print(Year[1])

        # The output file is a comma separated variable file with two columns, first the DOI URL, and second the date of publication. The date of publication is in YYYY-MM-DD format.
        output.write(url + "," + Year[1] + "\n")
    except:
        # print the URL and fail notice to the console
        print(url)
        print("FAIL")
        # add the URL that threw and error to the fail list
        fail.append(clean)

print("THE FOLLOWING DOIs DID NOT RESOLVE\n")
print(fail)
print("END")
output.close()
