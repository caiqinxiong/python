from django.shortcuts import render, redirect,HttpResponse
import pymysql


def classes(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        print(request.POST)
        v = request.POST.get('title')
        if len(v) > 0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("insert into class(title) values(%s)", [v, ])
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/classes/')
        else:
            return render(request, 'add_class.html',{'msg':'班级名称不能为空'})

def del_class(request):
    nid = request.GET.get('nid')

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s", [nid, ])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id = %s", [nid, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result)
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id = %s", [title, nid, ])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/classes/')


def students(request):
    """
    学生列表
    :param request: 封装请求相关的所有信息
    :return:
    """
    #
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(
        "select student.id,student.name,class.title from student left JOIN class on student.class_id = class.id")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'students.html', {'student_list': student_list})


def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()

        return render(request, 'add_student.html', {'class_list': class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name,class_id) values(%s,%s)", [name, class_id, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/students/')

from utils import sqlheper
def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        class_list = sqlheper.get_list("select id,title from class",[])
        current_student_info = sqlheper.get_one('select id,name,class_id from student where id=%s',[nid,])
        return render(request,'edit_student.html',{'class_list': class_list,'current_student_info':current_student_info})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlheper.modify('update student set name=%s,class_id=%s where id=%s',[name,class_id,nid,])
        return redirect('/students/')


# ############################ 对话框 ############################


def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sqlheper.modify('insert into class(title) values(%s)',[title,])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级标题不能为空')









