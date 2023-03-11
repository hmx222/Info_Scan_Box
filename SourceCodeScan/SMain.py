import SourceCodeScan.SMF
import requests
import function

requests.packages.urllib3.disable_warnings()


def SourceScan(aUrl:list, headers):
    wUrl = []

    for eu in aUrl:
        get = SourceCodeScan.SMF.Ping(eu)  # 拿到网页源代码
        email = function.SearchEmail(get)  # 对email的查找
        phone = function.SearchPhone(get)  # 对电话号码查找
        geturl:str = function.extract_URL(get)  # 对于网页源代码当中url的筛选(初次)
        for a_url in geturl:
            geturl = function.check_Url(a_url, eu)
            try:
                function.SearchBlackList(geturl)
            except:
                continue
            else:
                wUrl.append(geturl)
        path = function.SearchPath(get)  # 对于path内容的搜索
        ann = function.searCha(eu)  # 对注释的搜索

        writeType = input("How to write in ? (you can chose a/w)")
        print("以下是来自", eu, "的url：")
        for eUrl in wUrl:
            try:
                response = requests.get(eUrl, headers, verify=False, timeout=8).status_code
            except:
                print(eUrl, "NullStatus")
            else:
                if " " in eUrl:
                    eUrl = eUrl.replace(" ", "")
                function.write(eUrl,writeType)
                print(eUrl, "-" * 5, response)

        function.write("以下是来自"+ eu+"的路径：","a")
        print("以下是来自"+ eu+"的路径：",writeType)
        for pa1 in path:
            function.write("#"+pa1,writeType)
            print(pa1)
        function.write("以下是来自"+ eu+ "的注释：","a")
        for ann1 in ann:
            function.write("#"+ann1,"a")
            print(ann1)
        print("以下是来自", eu, "的email：")
        for em in email:
            function.write("#"+em,"a")
            print(em)
        print("以下是来自", eu, "的phone：")
        for ph in phone:
            function.write("#"+ph,"a")
            print(ph)

