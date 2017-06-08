# importing csv module
import csv
import json
import sys
import requests
import os
from time import sleep
from subprocess import check_output
VNFID="ff17f286-0f8a-4e8e-aef0-20ceaea81845"
 
# initializing the titles and rows list
START = 0
END = 0
def get_the_pid_of_process(name):
	return check_output(["pidof",name])

try:
	x=get_the_pid_of_process("sipp").strip("\n")
except:
	#if (int(x) == 0):
	print("sipp script is not running.First start the sipp script\n")
	sys.exit(0)
else:
    log_file_name="uas_core1_tas_reg_invite_" + x + "_logs.log"
    cmd="cat " + log_file_name + " > numbers.csv"
    print("pid of sipp is %s and log file name is %s\n"%(x,log_file_name))
    

while True:
    print("starting line number is %d\n"%START)
    sleep(5)
    csvfile = open(log_file_name, 'r')
    rows = []
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    END = csvreader.line_num
    csvfile.close()
    print("ending line number is %d\n"%END)
    file1 = os.stat(log_file_name)
    file1_size = file1.st_size
    for row in rows[START:]:
        for col in row:
            KEY=col[16:].strip("'").strip(">")
            MSISDN=col[4:14]
            content='{"keyId":"%s","keyId":"%s","vnfId":"%s"}' % (MSISDN,KEY,VNFID)
            content2='{"keyInformation":%s}' % (content)
            headers={'Content-Type': 'application/json'}
            response=requests.post("http://192.168.21.107:8001/vlb/anchor/v1/",data=content2,headers=headers)

    sleep(5)
    file2 = os.stat(log_file_name)
    file2_size = file2.st_size
    comp = file2_size - file1_size
    if comp == 0:
        print("exiting the infinite loop as there is no change in " + log_file_name)
        sys.exit(0)
    else:
        START=END
        print("continuing the while loop\n")
    
