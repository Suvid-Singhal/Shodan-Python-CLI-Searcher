#!/bin/env python

import subprocess, os
from shodan import Shodan

api = Shodan('YOUR-API-KEY-HERE')

while (True):
	print("\n*********************************")
	print("Welcome to CLI Shodan Searcher!!!")
	print("*********************************\n")
	print("1) What is my IP?")
	print("2) Search for a Host")
	print("3) Shodan Search to scan IPs, Hostnames, ports")
	print("\nPress CTRL+C to Exit")
	print("\nEnter your selection: \n")
	selection = int(input())
	if selection == 1:
	    print("\nYour IP Address:\n")
	    os.system("host myip.opendns.com resolver1.opendns.com | grep 'myip.opendns.com has' | awk '{print $4}'")
	    print("\n")
	if selection == 2:
	    print("\nInput Host ip address: ")
	    ip = input()
	    print("\nPress q to exit")
	    host = api.host(ip)
	    print("\n{}".format(host.get('ip_str')))
	    print("\nHostnames:				{}".format(', '.join(host.get('hostnames'))))
	    print("City:					{}".format(host.get('city')))
	    print("Country:				{}".format(host.get('country_name')))
	    print("Organization:				{}".format(host.get('org')))
	    print("Number of open ports:	{}".format(len(host.get('ports'))))
	    print("Ports:")
	    portsvisited=[]
	    for i in host['data']:
	    	if 'product' in i:
	    		if i.get('port') not in portsvisited:
	    			print("	{} 		{}".format(i['port'], i['product']))
	    			portsvisited.append(i.get('port'))
	    		else:
	    			continue
	    	if 'port' in i:
	    		if i.get('port') not in portsvisited:
	    			print("	{} ".format(i['port']))
	    			portsvisited.append(i.get('port'))
	    		else:
	    			continue
	    	else:
	    		continue
	if selection == 3:
	    print("\nInput your query to search: \n")
	    strinng = input()
	    results = api.search(strinng)
	    print('\nResults found: {}\n'.format(results['total']))
	    for result in results['matches']:
	    	print('{}	{}	{}	{}'.format(result.get('ip_str',"Not Found"), result.get('port',"Not Found"), result.get('org',"Not Found"), ', '.join(result.get('hostnames',"Not Found"))))
