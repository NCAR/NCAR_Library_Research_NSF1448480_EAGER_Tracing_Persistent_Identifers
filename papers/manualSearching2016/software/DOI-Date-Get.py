# Code by Matt Mayernik, mayernik@ucar.edu
# Written in Python 3.3
# This script takes in a list of DOIs, and returns the dates of publication for those DOIs

import urllib
from urllib.request import Request, urlopen
from urllib.error import  URLError
import re

file_name = ''      #INSERT THE APPROPRIATE FILE NAME

file = open(file_name).readlines()

# the output of this script is a file named FILENAME_out.txt, where FILENAME is the same as the original input filename
output = open(file_name, "w")

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
    # clean up the line in the data file
    strline = str(line)
    cleanline = re.sub("\n", "", strline)

    # split out the variables
    Vars = re.split(',',cleanline)
    DOI = Vars[0]
    Ref_Code = Vars[1]
    Paper_Type = Vars[2]

    if DOI[:3] != "10.":
        Year = "NA"
        print("Gray Lit - NA")
        output.write(DOI + "," + Ref_Code + "," + Paper_Type + "," + Year + "\n")

    else:
    
        # Query DOI service for the DOI metadata
        url = "http://dx.doi.org/" + DOI
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
            
            # Find the date string by finding it in the returned XML
            #Y_string = re.findall(".+http://www.w3.org/2001/XMLSchema#gYearMonth.+",m)
            Year_string = re.findall(".+http://www.w3.org/2001/XMLSchema#.+",m)
            Date_info = re.split("\"",Year_string[0]) #Needs to be a string
            Year = Date_info[1]
            
            # print the URL and date in the console so that you can see the script proceeding through the DOI list
            print(url)
            print(Year)

            # The output file is a comma separated variable file with two columns, first the DOI URL, and second the date of publication. The date of publication is in YYYY-MM-DD format.
            output.write(DOI + "," + Ref_Code + "," + Paper_Type + "," + Year + "\n")
        except:
            # print the URL and fail notice to the console
            print(url)
            print("FAIL")
            # add the URL that threw an error to the fail list
            fail.append(DOI)


print("THE FOLLOWING DOIs DID NOT RESOLVE\n")
print(fail)

print("END")
output.close()
