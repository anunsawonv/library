from django.shortcuts import render, redirect
from user.models import *
from library.models import *
# Create your views here.

def allBooks(request):
    allbooks = LmsAllbooks.objects.all()
    if allbooks:
        for obj in allbooks:
            catid = LmsCategory.objects.get(catid=obj.catid)
            class_id = LmsClassification.objects.get(class_id=obj.class_id)
            obj.catid = catid
            obj.class_id = class_id
    return render(request, 'LMS/allbooks.html', {'allbooks': allbooks})


def borrow(request, nid):
    # allbooks = LmsAllbooks.objects.get(book_id=nid)
    user = request.session['login_info'].get('lrn_no')
    date = datetime.datetime.today().date()
    dateuntil = date + datetime.timedelta(days=3)
    LmsLogs.objects.create(book_id=nid, lrn_no=user, status="Borrowed", datetrack=date, dateuntil=dateuntil)
    return redirect('/amsai/lms/books/')


def myBorrowedBooks(request):
    record = LmsStudentrecord.objects.get(lrn_no=request.session['login_info'].get('lrn_no'))
    status = "Borrowed"
    logs = LmsLogs.objects.filter(lrn_no=record.lrn_no, status=status).order_by('-datetrack')
    if logs:
        for obj in logs:
            book = LmsAllbooks.objects.get(book_id=obj.book_id)
            obj.book = book
    return render(request, 'LMS/user_borrowed.html', {'logs': logs})


def nonBorrowedBooks(request):
    record = LmsNonstudent.objects.get(username=request.session['login_info'].get('username'))
    status = "Borrowed"
    logs = LmsLogs.objects.filter(lrn_no=record.username, status=status).order_by('-datetrack')
    if logs:
        for obj in logs:
            book = LmsAllbooks.objects.get(book_id=obj.book_id)
            obj.book = book
    return render(request, 'LMS/user_borrowed.html', {'logs': logs})


def myReturnedBooks(request):
    record = LmsStudentrecord.objects.get(lrn_no=request.session['login_info'].get('lrn_no'))
    status = "Returned"
    logs = LmsLogs.objects.filter(lrn_no=record.lrn_no, status=status).order_by('-datetrack')
    if logs:
        for obj in logs:
            book = LmsAllbooks.objects.get(book_id=obj.book_id)
            obj.book = book
    return render(request, 'LMS/user_returned.html', {'logs': logs})


def nonReturnedBooks(request):
    record = LmsNonstudent.objects.get(username=request.session['login_info'].get('username'))
    status = "Returned"
    logs = LmsLogs.objects.filter(lrn_no=record.username, status=status).order_by('-datetrack')
    if logs:
        for obj in logs:
            book = LmsAllbooks.objects.get(book_id=obj.book_id)
            obj.book = book
    return render(request, 'LMS/user_returned.html', {'logs': logs})


def Events(request):
    event = LmsEvents.objects.all()
    return render(request, 'LMS/events.html', {'event': event})


def addEvents(request):
    if request.method == 'GET':
        return render(request, 'LMS/events_add.html')
    if request.method == 'POST':
        item = LmsEvents()
        item.date_posted = datetime.datetime.now().date()
        if len(request.FILES) != 0:
            item.image = request.FILES['image']

        item.save()
        return redirect('/amsai/lms/events/')


def Announcement(request):
    announce = LmsAnnouncement.objects.all()
    return render(request, 'LMS/announcement.html', {'announce': announce})