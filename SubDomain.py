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


def PingTest(url:list, header, lines):
    for k in url:
        for i in lines:
            if url[:7] == "http://":
                if url[7:11] == "www.":
                    com_url = k[:7] + i + "." + k[11:]
                else:
                    com_url = k[:7] + i + "." + k[7:]

            elif url[:8] == "https://":
                if url[8:12] == "www.":
                    com_url = k[:8] + i + "." + k[12:]
                else:
                    com_url = k[:8] + i + "." + k[8:]
            else:
                com_url = None

            try:
                response = requests.get(url=com_url, headers=header, verify=False).status_code
            except:
                continue
            else:
                if 200 <= response < 300:
                    function.write(k+"---"+response)
                    print(k, "-----", response)
                elif 300 <= response < 400:
                    function.write(k+"-----"+response)
                    print(k, "-----", response)
                elif 400 <= response < 500:
                    function.write(k+"-----"+response)
                    print(k, "-----", response)


