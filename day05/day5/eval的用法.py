def parser_contidion(condition,sep,symbol):
    col, val = condition.split(sep)
    ind = col_lst.index(col)
    for lst in file_lst:
        num = float(lst[ind].strip('%'))
        if eval('num %s val'%symbol):
            print(lst)
def dealwith_data():
    with open(r'D:\pycharm\py27\date4\frame',encoding='utf-8')as f:
        line = f.read()
        col_lst =line.split('\t')
    file_lst=[]
    with open(r'D:\pycharm\py27\date4\info',encoding='utf-8')as f:
        for line in f :
            line = line.strip()
            lst = line.split('\t')
            file_lst.append(lst)
    return col_lst,file_lst
def entry_point():
    condition = input('<<<')
    if '>' in condition:
        parser_contidion(condition,'>','>')
    elif '<' in condition:
        parser_contidion(condition, '<', '<')
    elif '=' in condition:
        parser_contidion(condition, '=', '==')
col_lst,file_lst =dealwith_data()
entry_point()
