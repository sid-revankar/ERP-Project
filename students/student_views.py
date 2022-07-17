from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "student-home.html")


def postFeedback(request):
    if request.method == 'POST':
        feedback.objects.create(
            name=request.POST.get("name"),
            reg_no=request.POST.get("reg_no"),
            semester=request.POST.get("sem"),
            about=request.POST.get("about"),
            created_at=request.POST.get("date"),
            body=request.POST.get("body"),
        )

        messages.success(
            request, 'Your feedback is posted and will be considered!')
        return redirect('/student')
    return render(request, 'post_feedback.html')


@login_required
def sem1StudentsDelete(request):
    if request.user.is_superuser:
        Sem1Students.objects.all().delete()
        messages.success(request, 'All Semester-1 student records deleted!')
        return redirect('/students/details/1')


@login_required
def sem2StudentsDelete(request):
    if request.user.is_superuser:
        Sem2Students.objects.all().delete()
        messages.success(request, 'All Semester-2 student records deleted!')
        return redirect('/students/details/2')


@login_required
def sem3StudentsDelete(request):
    if request.user.is_superuser:
        Sem3Students.objects.all().delete()
        messages.success(request, 'All Semester-3 student records deleted!')
        return redirect('/students/details/3')


@login_required
def sem4StudentsDelete(request):
    if request.user.is_superuser:
        Sem4Students.objects.all().delete()
        messages.success(request, 'All Semester-4 student records deleted!')
        return redirect('/students/details/4')


@login_required
def sem5StudentsDelete(request):
    if request.user.is_superuser:
        Sem5Students.objects.all().delete()
        messages.success(request, 'All Semester-5 student records deleted!')
        return redirect('/students/details/5')


@login_required
def sem6StudentsDelete(request):
    if request.user.is_superuser:
        Sem6Students.objects.all().delete()
        messages.success(request, 'All Semester-6 student records deleted!')
        return redirect('/students/details/6')
