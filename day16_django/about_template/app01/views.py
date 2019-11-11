from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    l = [11, 22, 33]
    d = {"name": "alex",'keys':'xxxx'}

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def dream(self):
            return "{} is dream...".format(self.name)

    Alex = Person(name="Alex", age=34)
    Egon = Person(name="Egon", age=9000)
    Eva_J = Person(name="Eva_J", age=18)

    person_list = [Alex, Egon, Eva_J]
    return render(request, "index.html", {
        "l1": l,
        "d": d,
        "person_list": person_list,
        'xxx':{},
        'filesize':1024*1024*1024*1024*1024*1024,
        'now':datetime.datetime.now(),
        'a':'<a href="https://www.luffycity.com">路飞</a>'
    })