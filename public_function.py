def List_con(listTemp, n):
    for i in range(0, len(listTemp), n):
        yield listTemp[i:i + n]


def Read(filename):
    lines = []
    file = open(filename, 'r',encoding='utf-8')
    while True:
        text = file.readline().strip()
        if not text:
            break
        lines.append(text)
    file.close()
    return lines
