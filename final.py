#!/bin/env python

import subprocess,os

while(True):
	print("*********************************")
	print("Welcome to CLI Shodan Searcher!!!")
	print("*********************************\n")
	print("1) What is my IP?")
	print("2) Search for a Host")
	print("3) Shodan Search to scan IPs, Hostnames, ports")
	print("Press CTRL+C to Exit")
	print("Enter your selection: ")
	selection = int(input())
	if selection == 1:
		print("Your IP Address:")
		os.system('shodan myip')
	if selection == 2:
		print("Input Host ip address: ")
		ip = input()
		print("Press q to exit")
		os.system('shodan host '+ip)
	if selection == 3:
		print("Input your have query to searching: ")
		query = input()
		print("Press q to exit")
		os.system('shodan search --fields ip_str,port,org,hostnames '+query)
