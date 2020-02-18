from django.shortcuts import render
msg = []

def comment(request):
    if request.method == "GET":
        return render(request,'comment.html')
    else:
        v = request.POST.get('content')
        if "script" in v:
            return render(request,'comment.html',{'error': '小比崽子还黑我'})
        else:
            msg.append(v)
            return render(request,'comment.html')

def index(request):
    return render(request,'index.html',{'msg':msg})

def test(request):
    from django.utils.safestring import mark_safe
    temp = "<a href='http://www.baidu.com'>百度</a>"
    newtemp = mark_safe(temp)
    return render(request,'test.html',{'temp':newtemp})