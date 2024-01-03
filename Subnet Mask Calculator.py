import ipaddress
import csv

with open('ips.csv') as file:
    reader = csv.reader(file)
    count = 0
    print("computers not in the subnet:")
    for row in reader:
        if (ipaddress.ip_address(row[0]) in ipaddress.ip_network('10.1.0.0/16')):
            print ("",end = "") 
        elif (ipaddress.ip_address(row[0]) in ipaddress.ip_network('10.129.0.0/13',False)):
            print ("",end = "")
        elif (ipaddress.ip_address(row[0]) in ipaddress.ip_network('10.128.128.0/22')):
            print ("",end = "")
        elif (ipaddress.ip_address(row[0]) in ipaddress.ip_network('10.128.0.0/24')):
            print ("",end = "")
        elif (ipaddress.ip_address(row[0]) in ipaddress.ip_network('10.6.0.0/16')):
            print ("",end = "")
        else:
            print(row[0])
        count=count+1
    print(count)
    
    