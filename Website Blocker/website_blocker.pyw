import time
from datetime import datetime as dt

# Relative path for hosts file
host_path = r'C:\Windows\System32\drivers\etc\hosts'
host_temp = r'C:\Users\Anurag\Desktop\python\python_projects\Website Blocker\hosts'

#Redirect IP address
redirect = '127.0.0.1'
#Websites that needs to be blocked
website_list = ['www.facebook.com','facebook.com','www.youtube.com','youtube.com']

#Comparing current time with working hours in this case [8am - 4pm]
#Redirecting the blocked websites to localhost
while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <
    dt(dt.now().year,dt.now().month,dt.now().day,16)):
        #print('working hours..')
        with open(host_path,'r+') as file:
            content = file.read()
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write(redirect+" "+websites+"\n")
    else:                   #Unblocking the websites after or before working hours
        #print('fun hours..')
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(5)
