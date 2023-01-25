import re


def SearchUrl(context):  # 对于网站url的筛选
    ex = '(https?://.*?\.[php|asp|aspx|jsp|json|action|html|js|txt|xml])'  # 对于网站类型的查找
    response = re.findall(ex, context)
    return response


def SearchPhone(content):
    phone = "^1(3[0-9]|5[0-3,5-9]|7[1-3,5-8]|8[0-9])\d{8}$"  # 对于电话号码的查找
    response = re.findall(phone, content)
    return response


def SearchEmail(content):
    email = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'  # 对于邮箱的查找
    response = re.findall(email, content)
    return response


def SearchPath(content):
    new_list = []
    path = 'path:"(.*?)"'
    href = 'href="(.*?)"'
    src = 'src="(.*?)"'
    list = [path,href,src]
    for i in list:
        demo_list = re.findall(i,content)
        new_list.extend(demo_list)
    return demo_list

def Searchann(content):
    annotation = '(<!-- .*? -->)'
    response=re.findall(annotation,content)
    return response

def SearchEveryUrl(content):  # 更加强大的筛选
    path = '(https?://.*?)["|\>|\']'
    response = re.findall(path, content)
    return response


def SearchOtherPa(content):
    new_list=[]
    path = '"(//?[A-Za-z0-9-\.]+/[A-Za-z0-9-\.#\?\=]+)"'  # 一级
    path2 = '"(//?[A-Za-z0-9-\.]+/[A-Za-z0-9-]+/[A-Za-z0-9-\.#\?\=]+)"'  # 二级
    path3 = '"(//?[A-Za-z0-9-\.]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-\.#\?\=]+)"'  # 三级
    path4 = '"(//?[A-Za-z0-9-\.]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-\.#\?\=]+)"'  # 四级
    path5 = '"(//?[A-Za-z0-9-\.]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-\.#\?\=]+)"'  # 五级
    path6 = '"(//?[A-Za-z0-9-\.]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-]+/[A-Za-z0-9-\.#\?\=]+)"'  # 六级
    list = [path, path2, path3, path4, path5, path6]
    for i in list:
        demo_list = re.findall(i, content)
        new_list.extend(demo_list)
    return new_list


def SearchGovern(url):
    rex = '.*?gov\.cn'
    response = re.match(rex, url)
    if response:
        print("我们发现了政府网站，准备抛出异常")
        raise RuntimeError('政府网站--Error')

