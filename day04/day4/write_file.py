while True:
    f = open('test', 'a', encoding='utf-8')
    content = input('>>>')
    f.write(content)
    f.close()
