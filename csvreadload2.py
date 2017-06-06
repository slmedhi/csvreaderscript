# importing csv module
import csv
import json
import sys
import requests
import os
from time import sleep
VNFID="ff17f286-0f8a-4e8e-aef0-20ceaea81845"
# csv file name
filename = "numbers.csv"
 
# initializing the titles and rows list
fields = []
START = 0
END = 0

#with open(filename, 'r') as csvfile:
while True:
    csvfile = open(filename, 'r')
    rows = []
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    #fields = csvreader.next()
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    END = csvreader.line_num
    csvfile.close()
    file1 = os.stat('numbers.csv')
    file1_size = file1.st_size
    print("%d\n"%END)
    for row in rows[START:]:
        for col in row:
            #print("%10s"%col)
            KEY=col
            #KEY=str(sys.argv[1])[16:].strip("'").strip(">")
            MSISDN=KEY[4:14]
            content='{"keyId":"%s","keyId":"%s","vnfId":"%s"}' % (MSISDN,KEY,VNFID)
            content2='{"keyInformation":%s}' % (content)
            headers={'Content-Type': 'application/json'}
            response=requests.post("http://192.168.21.107:8001/vlb/anchor/v1/",data=content2,headers=headers)

    #file1 = os.stat('numbers.csv')
    #file1_size = file1.st_size
    sleep(5)
    file2 = os.stat('numbers.csv')
    file2_size = file2.st_size
    comp = file2_size - file1_size
    if comp == 0:
        print("exiting the infinite loop as there is no change in numbers.csv")
        sys.exit(0)
    else:
        START=END
        print("continuing the while loop\n")
    
