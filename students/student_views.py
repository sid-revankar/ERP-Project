from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def home(request):
    return render(request, "student-home.html")


def postFeedback(request):
    if request.method == 'POST':
        feedback_name = request.POST.get("name")
        feedback_reg_no = request.POST.get("reg_no")
        feedback_sem = request.POST.get("sem")
        feedback_about = request.POST.get("about")
        feedback_created_at = request.POST.get("date")
        feedback_body = request.POST.get("body")

        feedback.objects.create(
            name=feedback_name,
            reg_no=feedback_reg_no,
            semester=feedback_sem,
            about=feedback_about,
            created_at=feedback_created_at,
            body=feedback_body,
        )
        messages.success(
            request, 'Your feedback is posted and will be considered!')
        return redirect('/student')
    return render(request, 'post_feedback.html')