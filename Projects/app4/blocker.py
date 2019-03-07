from datetime import datetime as dt
import time

b_website=["www.facebook.com","gmail.com","www.gmail.com","fb.com"]
redirect="127.0.0.0"
# len=len(b_website)
# b=0

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
            print("WOrking hours",dt.now())
            with open (r"C:\Windows\System32\drivers\etc\hosts","r+") as file:
                content=file.read()
                for website in b_website:
                    if website in content:
                        print("website already there",dt.now())
                    else:
                        file.write(redirect+" "+website+"\n")
                        # len-=1
    else:
        with open(r"C:\Windows\System32\drivers\etc\hosts",'r+') as file:
            content=file.readlines()
            file.seek(0)
            print(content)
            for line in content:
                if not any(website in line for website in b_website):
                    file.write(line)
                file.truncate()
            print("Fun hours...",dt.now())

    time.sleep ( 5 )



    # # print(a)
    #
    #     time.sleep(5)


# a=strftime(dt.now())
# print(a)
