import re


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


def SearchPhone(content):
    phone = "^1(3[0-9]|5[0-3,5-9]|7[1-3,5-8]|8[0-9])\d{8}$"  # 对于电话号码的查找
    response = re.findall(phone, content)
    return response


def SearchEmail(content):
    email = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'  # 对于邮箱的查找
    response = re.findall(email, content)
    return response



def Searchann(content):
    annotation = '(<!-- .*? -->)|[^\x00-\xff]'
    response = re.findall(annotation, content)
    return response


def SearchEveryUrl(content):  # 更加强大的筛选
    path = '(https?://.*?)["|\>|\']'
    response = re.findall(path, content)
    return response


def SearchPath(content):
    rex = '[\'"](\/[^<>/\\\|:""\\ *\?]+){2,}[\'"]'
    response = re.findall(rex,content)
    return response


def SearchBlackList(url):
    rex = '(.*?gov\.cn)|(http://www.w3.org)'
    response = re.match(rex, url)
    if response:
        raise RuntimeError('黑名单网站--Error')
