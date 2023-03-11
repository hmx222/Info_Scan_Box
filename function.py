import re


def list_con(listTemp, n):
    for i in range(0, len(listTemp), n):
        yield listTemp[i:i + n]


def Read(filename):
    lines = []
    file = open(filename, 'r', encoding='utf-8')
    while True:
        text = file.readline().strip()
        if not text:
            break
        if text[0] == "#":
            continue
        text = text.split(" ")[0]
        lines.append(text)
    file.close()
    return lines

def write(content:str, type: str):
    f = open('urls.txt', type)
    f.write(content)
    f.close()

def extract_URL(JS):
    pattern_raw = r"""
	  (?:"|')                               # Start newline delimiter
	  (
	    ((?:[a-zA-Z]{1,10}://|//)           # Match a scheme [a-Z]*1-10 or //
	    [^"'/]{1,}\.                        # Match a domainname (any character + dot)
	    [a-zA-Z]{2,}[^"']{0,})              # The domainextension and/or path
	    |
	    ((?:/|\.\./|\./)                    # Start with /,../,./
	    [^"'><,;| *()(%%$^/\\\[\]]          # Next character can't be...
	    [^"'><,;|()]{1,})                   # Rest of the characters can't be
	    |
	    ([a-zA-Z0-9_\-/]{1,}/               # Relative endpoint with /
	    [a-zA-Z0-9_\-/]{1,}                 # Resource name
	    \.(?:[a-zA-Z]{1,4}|action)          # Rest + extension (length 1-4 or action)
	    (?:[\?|/][^"|']{0,}|))              # ? mark with parameters
	    |
	    ([a-zA-Z0-9_\-]{1,}                 # filename
	    \.(?:php|asp|aspx|jsp|json|
	         action|html|js|txt|xml)             # . + extension
	    (?:\?[^"|']{0,}|))                  # ? mark with parameters
	  )
	  (?:"|')                               # End newline delimiter
	"""
    pattern = re.compile(pattern_raw, re.VERBOSE)
    result = re.finditer(pattern, str(JS))
    if result == None:
        return None
    js_url = []
    return [match.group().strip('"').strip("'") for match in result
            if match.group() not in js_url]


def check_Url(url, geturl):
    if url[:2] == "//":
        if geturl[:7] == "http://":
            url = "http://" + url
            return url
        if geturl[:8] == "https:":
            url = "https:" + url
            return url
    if url[:1] == "/":
        if geturl[:7] == "http://":
            url = "http:/" + url
            return url
        if geturl[:8] == "https:":
            url = "https:/" + url
            return url


def SearchPhone(content):
    phone = "^1(3[0-9]|5[0-3,5-9]|7[1-3,5-8]|8[0-9])\d{8}$"  # 对于电话号码的查找
    response = re.findall(phone, content)
    return response


def SearchEmail(content):
    email = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'  # 对于邮箱的查找
    response = re.findall(email, content)
    return response


def searCha(content):
    annotation = '(<!-- .*? -->)|[^\x00-\xff]'
    response = re.findall(annotation, content)
    return response


def SearchPath(content):
    rex = '[\'"](\/[^<>/\\\|:""\\ *\?]+){2,}[\'"]'
    response = re.findall(rex, content)
    return response


def SearchBlackList(url):
    black_list = Read("black.txt")
    for i in black_list:
        if i in url:
            raise ValueError("黑名单")


def Ana(content):
    response = re.findall("<TD>(.*?)<\/TD>", content)
    return response


def tileScan(content):
    response = re.findall("<title>(.*?)</title>",content)
    return response