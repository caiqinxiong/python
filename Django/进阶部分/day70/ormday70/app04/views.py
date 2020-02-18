from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def login(request):
    if request.method == "POST":
        # 取出数据
        user = request.POST.get("username")
        pwd = request.POST.get("pwd")

        if user == "alex" and pwd =="dsb":
            return redirect("http://www.luffycity.com")

    return render(request, "login.html")


# 转账
def transfer(request):
    if request.method == "POST":
        from_ = request.POST.get("from")
        to_ = request.POST.get("to")
        money = request.POST.get("money")

        print("{} 给 {} 转了 {}钱".format(from_, to_, money))
        return HttpResponse("转账成功！")

    return render(request, "transfer.html")
