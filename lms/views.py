from django.shortcuts import render
from lms.forms import UserForm, UserProfileInfoForm ,UserForm1, UserProfileInfoForm1,course
from lms.models import UserProfileInfo ,Instructor,courseforms
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Users
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'lms/index.html')


def dashboard(request):
    return render(request, 'lms/dashboard.html')


def course1(request):
    return render(request, 'lms/ethical.html')


def course2(request):
    return render(request, 'lms/mysql.html')


def course3(request):
    return render(request, 'lms/writing.html')


def course4(request):
    return render(request, 'lms/guitar.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def course5(request):
    return render(request, 'lms/german.html')


def course6(request):
    return render(request, 'lms/microcontroller.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()


            registered = True
            return render(request, 'lms/login2.html')
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'lms/registration2.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'lms/dashboard2.html')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print("username:{} and password {}".format(username, password))
            return HttpResponse("invalid login ")
    else:
        return render(request, "lms/login2.html", {})


def dashboard2(request):
    return render(request, 'lms/dashboard2.html')
def dashboard3(request):
    return render(request, 'lms/dashboard3.html')

def profile(request):
    details=UserProfileInfo.objects.filter(user=request.user)
    return render(request,'lms/profile4.html',{'detail':details})
def profile2(request):
    details=Instructor.objects.filter(user=request.user)
    return render(request,'lms/profile5.html',{'detail':details})

def option(request):
    return render(request, 'lms/option.html')
def option2(request):
    return render(request, 'lms/option2.html')
def coursesenrolled(request):
    return render(request, 'lms/courses.html')
def achievement(request):
    return render(request, 'lms/achievement.html')
def coursesenrolled1(request):
    return render(request, 'lms/courses1.html')
def achievement1(request):
    return render(request, 'lms/achievement1.html')
def v(request):
    return render(request,'lms/viewcourse.html')



def register1(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm1(data=request.POST)
        profile_form = UserProfileInfoForm1(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()


            registered = True
            return render(request, 'lms/login3.html')
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm1()
        profile_form = UserProfileInfoForm1()

    return render(request, 'lms/registration2.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'registered': registered})


def user_login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'lms/dashboard3.html')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print("username:{} and password {}".format(username, password))
            return HttpResponse("invalid login ")
    else:
        return render(request, "lms/login3.html", {})
@csrf_exempt
def courseregister(request):
    registered = False

    if request.method == "POST":
        user_form = course(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user

            # profile.save()


            registered = True
            return render(request, 'lms/dashboard3.html')
        else:
            print(user_form.errors)

    else:
        user_form = course()
        # profile_form = UserProfileInfoForm()

    return render(request, 'lms/registration3.html', {'user_form': user_form,'registered': registered})
def courseinfo(request):
    details=courseforms.objects.all()
    return render(request,'lms/info.html',{'detail':details})
