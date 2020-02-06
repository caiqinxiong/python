from django.shortcuts import render,redirect
import pymysql
def classes(request):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request,'classes.html',{'class_list': class_list})

def add_class(request):
    if request.method == "GET":
        return render(request,'add_class.html')
    else:
        print(request.POST)
        v = request.POST.get('title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(title) values(%s)",[v,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def del_class(request):
    nid = request.GET.get('nid')

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s",[nid,])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')

def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id = %s",[nid,])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result)
        return render(request,'edit_class.html',{'result':result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id = %s",[title,nid,])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/classes/')