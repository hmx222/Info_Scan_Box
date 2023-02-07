import requests
import public_function
from concurrent.futures import ThreadPoolExecutor, Future

def Readfold(option):
    if option == 1:
        lines = public_function.Read("folder/logical.txt")
        return lines
    elif option == 2:
        lines = public_function.Read("folder/illogical.txt")
        return lines

def PingTest(url, header,lines):
    for i in lines:
        url = i + "." + url
        try:
            response = requests.get(url=url, headers=header,timeout=8).status_code
        except:
            continue
        else:
            if 200 <= response < 300:
                print(url,"---",response)
            elif 300 <= response < 400:
                print(url,"---",response)
            elif 400 <= response < 500:
                print(url,"---",response)

