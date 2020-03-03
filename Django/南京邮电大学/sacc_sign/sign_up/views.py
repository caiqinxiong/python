from django.shortcuts import render
from .forms import TeamInfoForm
from .models import Team_info,Actor_info
from users.models import User
from django.http import HttpResponseRedirect,Http404 #用户提交主题后我们将使用这个类将用户重新定向到网页topics
from django.urls import reverse #该函数根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成url
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    try:
        actor_info = Actor_info.objects.get(actor_id=request.user)
    except:
        actor_info = None
    context = {'actor_info':actor_info}
    return render(request, 'sign_up/home.html',context)

@login_required
def new_team(request):
    if request.method != 'POST':
        new_team = TeamInfoForm()
    else:
        new_team = TeamInfoForm(data=request.POST)
        user = User.objects.get(username=request.user)
        actor_info = Actor_info.objects.get(actor_id=request.user)
        if actor_info.is_added == True:
            context = {'actor_info':actor_info}
            return render(request,'sign_up/is_added_error.html',context)
        if new_team.is_valid():
            new_team = new_team.save(commit=False)
            new_team.leader = user.name
            new_team.leader_college = user.college
            new_team.leader_tel = user.tel
            new_team.leader_id = user.username
            new_team.leader_email = user.email
            new_team.owner = request.user
            new_team.save()
            Actor_info.objects.filter(actor_id=request.user).update(
                is_added=True, team_name=new_team.team_name
            )
            return HttpResponseRedirect(reverse('sign_up:index'))
    context = {'new_team': new_team}
    return render(request, 'sign_up/new_team.html', context)

@login_required
def my_team(request):
    lname = [str(request.user), str(request.user), str(request.user)]
    query = "SELECT * FROM sign_up_team_info WHERE leader_id=%s OR student_id1=%s OR student_id2=%s"
    teams = Team_info.objects.raw(query, params=lname)
    user_id = request.user
    context = {'teams': teams,'user_id':str(user_id)}
    return render(request, 'sign_up/my_team.html', context)


@login_required
def delete_team(request,team_id):
    team = Team_info.objects.get(id=team_id)
    if team.owner == request.user:
        Actor_info.objects.filter(actor_id=team.student_id1).update(
            is_added=False, team_name=''
        )
        Actor_info.objects.filter(actor_id=team.student_id2).update(
            is_added=False, team_name=''
        )
        Actor_info.objects.filter(actor_id=team.leader_id).update(
            is_added=False, team_name=''
        )
        Team_info.objects.filter(id = team_id).delete()
    else:
        return render(request,'sign_up/delete_error.html')
    return render(request,'sign_up/delete_actor.html')


@login_required
def edit_team(request,team_id):
    team = Team_info.objects.get(id=team_id)
    if str(team.owner) != str(request.user):
        return render(request,'sign_up/edit_error.html')
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        team_key = request.POST.get('team_key')
        leader_college = request.POST.get('leader_college')
        leader_id = request.POST.get('leader_id')
        leader = request.POST.get('leader')
        leader_tel = request.POST.get('leader_tel')
        leader_email = request.POST.get('leader_email')
        college1 = request.POST.get('college1')
        student_id1 = request.POST.get('student_id1')
        member1 = request.POST.get('member1')
        tel1 = request.POST.get('tel1')
        email1 = request.POST.get('email1')
        college2 = request.POST.get('college2')
        student_id2 = request.POST.get('student_id2')
        member2 = request.POST.get('member2')
        tel2 = request.POST.get('tel2')
        email2 = request.POST.get('email2')
        Team_info.objects.filter(id=team_id).update(
            team_name= team_name,
            team_key = team_key,
            leader_college = leader_college,
            leader_id = leader_id,
            leader = leader,
            leader_tel = leader_tel,
            leader_email = leader_email,
            college1 = college1,
            student_id1 = student_id1,
            member1 = member1,
            tel1 = tel1,
            email1 = email1,
            college2 = college2,
            student_id2 = student_id2,
            member2 = member2,
            tel2 = tel2,
            email2 = email2,
        )
        return HttpResponseRedirect(reverse('sign_up:my_team'))
    context = {'team':team}
    return render(request,'sign_up/edit_actor.html',context)


@login_required
def add_team(request):
    if request.method == 'POST':
        team_key = request.POST.get('team_key')
        try:
            team = Team_info.objects.get(team_key=team_key)
        except:
            return render(request,'sign_up/add_team_error.html')
        actor_info = Actor_info.objects.get(actor_id=request.user)
        user = User.objects.get(username=request.user)
        if actor_info.is_added == True:
            context = {'actor_info':actor_info}
            return render(request,'sign_up/is_added_error.html',context)#############
        member = user.name
        college = user.college
        tel = user.tel
        student_id = user.username
        email = user.email
        if team.member1 is None or team.member1 is '':
            Team_info.objects.filter(team_key=team_key).update(
                member1=member, college1=college, tel1=tel, student_id1=student_id, email1=email
            )
            Actor_info.objects.filter(actor_id=request.user).update(
                is_added=True,team_name=team.team_name
            )
        elif team.member2 is None or team.member2 is '':
            Team_info.objects.filter(team_key=team_key).update(
                member2=member, college2=college, tel2=tel, student_id2=student_id, email2=email
            )
            Actor_info.objects.filter(actor_id=request.user).update(
                is_added=True, team_name=team.team_name
            )
        else:
            return render(request,'sign_up/add_team_error_1.html')

        return HttpResponseRedirect(reverse('sign_up:index'))
    else:
        return render(request,'sign_up/add_team.html')


@login_required
def quit_team(request,team_id):
    team = Team_info.objects.get(id=team_id)
    actor_info = Actor_info.objects.get(actor_id=request.user)
    user = User.objects.get(username=request.user)
    if actor_info.is_added == False:
        is_added = actor_info.is_added
        context = {'is_added':is_added}
        return render(request, 'sign_up/is_added_error.html',context)
    if team.student_id1 == actor_info.actor_id:
        Team_info.objects.filter(id=team_id).update(
            member1='', college1='', tel1='', student_id1='', email1=''
        )
        Actor_info.objects.filter(actor_id=request.user).update(
            is_added=False, team_name=''
        )
    else:
        Team_info.objects.filter(id=team_id).update(
            member2='', college2='', tel2='', student_id2='', email2=''
        )
        Actor_info.objects.filter(actor_id=request.user).update(
            is_added=False, team_name=''
        )
    return HttpResponseRedirect(reverse('sign_up:index'))


@login_required
def delete_member(request,member_id):
    team = Team_info.objects.get(owner=request.user)
    if member_id == '1':
        Team_info.objects.filter(owner=request.user).update(
            member1='', college1='', tel1='', student_id1='', email1=''
        )
        Actor_info.objects.filter(actor_id=team.student_id1).update(
            is_added=False, team_name=''
        )
    else:
        Team_info.objects.filter(owner=request.user).update(
            member2='', college2='', tel2='', student_id2='', email2=''
        )
        Actor_info.objects.filter(actor_id=team.student_id2).update(
            is_added=False, team_name=''
        )
    teams = Team_info.objects.filter(owner=request.user)
    user = request.user
    context = {'teams':teams,'user':user}
    return render(request,'sign_up/my_team.html',context)
