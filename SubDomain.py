import requests
import function
requests.packages.urllib3.disable_warnings()


def Readfold(option):
    if option == 1:
        lines = function.Read("folder/logical.txt")
        return lines
    elif option == 2:
        lines = function.Read("folder/illogical.txt")
        return lines


def PingTest(url, header, lines):

    for i in lines:
        if url[:7] == "http://":
            if url[7:11] == "www.":
                com_url = url[:7] + i + "." + url[11:]
            else:
                com_url = url[:7] + i + "." + url[7:]

        elif url[:8] == "https://":
            if url[8:12] == "www.":
                com_url = url[:8] + i + "." + url[12:]
            else:
                com_url = url[:8] + i + "." + url[8:]
        else:
            com_url = None

        try:
            response = requests.get(url=com_url, headers=header, verify=False).status_code
        except:
            continue
        else:
            if 200 <= response < 300:
                print(url, "---", response)
            elif 300 <= response < 400:
                print(url, "---", response)
            elif 400 <= response < 500:
                print(url, "---", response)


# PingTest("http://www.biancheng.net/",
#         {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
#      'referer': 'https://www.baidu.com',
#      "Connection": "close"},
#         ['a', 'b', 'c', 'd'])
