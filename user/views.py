import datetime, string, random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from library.models import LmsEvents, LmsAnnouncement
from user.models import *

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'is_active': True})
    if request.method == 'POST':
        account = request.POST.get("account")
        username = request.POST.get("username")
        password = request.POST.get("password")
        users = LmsNonstudent.objects.filter(username=username)
        admin = Users.objects.filter(username=username)
        if account == "Non-Student":
            if len(users):
                for user in users:
                    if password == user.password:
                        request.session['login_info'] = {'username': user.username, 'name': user.name,
                                                         'contact': user.contact, 'address': user.address,
                                                         'dateregistered': user.dateregistered, 'status': user.status}
                        print(1)
                        if request.session['login_info'].get('status') == 'Active':
                            return redirect('/amsai/lms/dashboard/')
                        elif request.session['login_info'].get('status') == 'Pending':
                            return redirect('/amsai/lms/')
                        else:
                            return render(request, 'home/page-403.html')
                    else:
                        return render(request, 'accounts/login.html', {'warn': 'The password entered is incorrect.'})
            else:
                return render(request, 'accounts/login.html', {'warn': 'You have entered an invalid username or password'})

        elif account == "Student":
            amsai = Student.objects.filter(lrn=username)
            student = LmsStudentrecord.objects.filter(lrn_no=username)
            if len(amsai):
                if len(student):
                    for user in student:
                        if username == user.lrn_no:
                            request.session['login_info'] = {'id': user.id, 'lrn_no': user.lrn_no, 'studentname': user.studentname,
                                                             'grade': user.grade}
                            print(1)
                            return redirect('/amsai/lms/dashboard/')
                        else:
                            return render(request, 'accounts/login.html', {'warn': 'The credentials you entered is incorrect.'})
                else:
                    for obj in amsai:
                        if username == obj.lrn:
                            studentname = obj.lastname
                            LmsStudentrecord.objects.create(lrn_no=obj.lrn, studentname=studentname, grade=obj.level)
                            request.session['login_info'] = {'lrn_no': obj.lrn, 'studentname': obj.lastname,
                                                             'grade': obj.level}
                            Student.objects.create()
                            return redirect('/amsai/lms/dashboard/')
                        else:
                            return render(request, 'accounts/login.html',
                                          {'warn': 'The credentials you entered is incorrect.'})
            elif len(student):
                    for user in student:
                        if username == user.lrn_no:
                            request.session['login_info'] = {'id': user.id, 'lrn_no': user.lrn_no, 'studentname': user.studentname,
                                                             'grade': user.grade}
                            print(1)
                            return redirect('/amsai/lms/dashboard/')
                        else:
                            return render(request, 'accounts/login.html', {'warn': 'The credentials you entered is incorrect.'})
            else:
                return render(request, 'accounts/login.html', {'warn': 'You have entered an invalid username or password'})

        if account == "Admin":
            if len(admin):
                for user in admin:
                    if password == user.password:
                        request.session['login_info'] = {'username': user.username, 'userrole': user.userrole,
                                                         }
                        print(1)
                        if request.session['login_info'].get('status') == 'Active':
                            return redirect('/amsai/lms/dashboard/')
                        elif request.session['login_info'].get('status') == 'Pending':
                            return redirect('/amsai/lms/')
                        else:
                            return render(request, 'home/page-403.html')
                    else:
                        return render(request, 'accounts/login.html', {'warn': 'The password entered is incorrect.'})
            else:
                return render(request, 'accounts/login.html', {'warn': 'You have entered an invalid username or password'})


def registerNonstudent(request):
    if request.method == 'GET':
        random_chars = ''.join(random.choices(string.digits, k=8))
        refno = f"{random_chars}"
        return render(request, 'accounts/nonstudent_register.html', {'refno': refno})
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        username = request.POST.get('username')
        password = request.POST.get('password')
        dateregistered = datetime.datetime.today().date()
        status = "Pending"
        check = LmsNonstudent.objects.filter(username=username)
        if check:
            return render(request, 'accounts/nonstudent_register.html', {'warn': "Username already exists."})
        else:
            LmsNonstudent.objects.create(name=name, address=address, contact=contact, username=username,
                                         dateregistered=dateregistered, status=status, password=password)
            messages.success(request, f'{username}')
            return redirect('/amsai/lms/nonstudent_register/')
    # return render(request, 'accounts/nonstudent_register.html', {'warn': "Complete the form"})


# @login_required(login_url="/amsai/lms/login/")
def index(request):
    return render(request, 'home/empty.html')


from datetime import timedelta
def dashboard(request):
    books = len(LmsAllbooks.objects.all())
    events = len(LmsEvents.objects.all())
    borrow = len(LmsLogs.objects.filter(status="Borrowed", datetrack=datetime.datetime.today().date()))
    cat = len(LmsCategory.objects.all())
    classf = len(LmsClassification.objects.all())
    date = datetime.datetime.today().date()
    item = LmsEvents.objects.all()
    announcement = LmsAnnouncement.objects.all().order_by('-id')[:2]
    fromyesterday = borrow - len(LmsLogs.objects.filter(status="Borrowed", datetrack=datetime.datetime.today().date()-timedelta(days=1)))
    return render(request, 'home/dashboard.html', {'books': books, 'events': events,
                                                   'borrow': borrow, 'date': date, 'cat': cat, 'classf': classf,
                                                   'fromyesterday': fromyesterday, 'item': item, 'announcement': announcement})


def profile(request):
    return render(request, 'accounts/my_profile.html')

def logout(request):
    request.session.clear()
    return redirect('/amsai/lms/login/')
