import ipaddress
import csv

with open('ips.csv') as file:
    reader = csv.reader(file)
    count = 0
    print("computers not in the subnet:")
    for row in reader:
        if (ipaddress.ip_address(row[0]) in ipaddress.ip_network('0.xxx.x.x/xx')):
            print ("",end = "") 
        elif (ipaddress.ip_address(row[0]) in ipaddress.ip_network('10.xxx.x.x/xx',False)):
            print ("",end = "")
            print(row[0])
        count=count+1
    print(count)
    
    
