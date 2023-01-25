import requests
import DirSearch


def PingTest(url, header, option):
    lines = []
    SubDoList200 = []
    SubDoList300 = []
    SubDoList400 = []

    if option == 1:
        DirSearch.Read("folder/logical.txt")
    elif option == 2:
        DirSearch.Read("folder/illogical.txt")

    for i in lines:
        url = i + "." + url
        try:
            response = requests.get(url=url, headers=header,timeout=8).status_code
        except:
            continue
        else:
            if 200 <= response < 300:
                SubDoList200.append(url)
            elif 300 <= response < 400:
                SubDoList300.append(url)
            elif 400 <= response < 500:
                SubDoList400.append(url)

    return SubDoList200, SubDoList300, SubDoList400
