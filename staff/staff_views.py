import os
import pandas as pd
from .models import *
from .forms import *
from students.models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# -----------------------------------------------------------------------


# common home
def home(request):
    return render(request, 'home.html')

# staff home


def staff_home(request):
    return render(request, 'staff/staff-home.html')

# custom login view


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/staff')
        else:
            messages.error(request, 'Invalid credentials login again.')
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


# -----------------------------------------------------------------------


'''
This function returns the data stored in the database ordered by time..
.filter() function is used to filter the records as per the user logged in and order_by() is used to order the records using the passed argument.
'''

# display timetable to specific user


@login_required
def display_tt(request):
    '''
    This function takes input from the timetable form and enters the input into the database.
    Function .create(), creates a new record into the database using the input data.
    Returns a success message to the template upon record creation.
    '''
    if request.method == 'POST':  # check post

        # get field values from html form and creates a new record

        Timetable.objects.create(
            user=request.user,
            semester=request.POST.get("semester"),
            subject=request.POST.get("subject"),
            room_no=request.POST.get("room"),
            time=request.POST.get("time"),
            day=request.POST.get("day"),
        )

        messages.success(
            request, 'Added record to the timetable successfully!')
        return redirect('/staff/time-table')

    # code to display records
    tt = Timetable.objects.filter(user=request.user).order_by('time')
    return render(request, 'staff/timetable/time_table.html', {'tt': tt})


# update view for timetable record
@login_required
def update_record(request, tt_id):

    # fetch the object related to passed id
    tt = Timetable.objects.get(pk=tt_id)

    # pass the object fields to a context dictionary
    context = {
        'sub': tt.subject,
        'sem': tt.semester,
        'room': tt.room_no,
        'time': tt.time,
        'weekday': tt.day,
    }

    if request.method == 'POST':  # check post request
        # get field values from html form
        # assign values to object fields
        tt.subject = request.POST.get("subject")
        tt.semester = request.POST.get("semester")
        tt.room_no = request.POST.get("room")
        tt.time = request.POST.get("time")
        tt.day = request.POST.get("day")

        # saves the records (overrides)
        tt.save()
        messages.success(request, 'Timetable updated successfully!')
        return redirect('/staff/time-table')

    # pass context dictionary to html template
    return render(request, "staff/timetable/update_tt.html", context)


'''
Function .delete(), deletes the row using the passed id of the row in the database.
The passed timetable id (tt_id) is used as primary key to delete the particular record.
'''

# view to delete specific timetable record


@login_required
def delete_record(request, tt_id):
    record = Timetable.objects.get(pk=tt_id).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/staff/time-table')


# --------------------------------------------------------------------


# view feedback posted by students
@login_required
def view_feedback(request):
    feed = feedback.objects.all()
    context = {'feed': feed}
    return render(request, 'staff/feedback/view_feedback.html', context)

# delete view for unwanted feedbacks


@login_required
def delete_feedback(request, f_id):
    record = feedback.objects.get(pk=f_id).delete()
    messages.success(request, 'Feedback deleted successfully!')
    return redirect('/staff/feedback')


# --------------------------------------------------------------------


# attendance home view
@login_required
def attendance(request):
    return render(request, 'staff/attendance/attendance-home.html')

# semester 1 attendance view


@login_required
def sem1Attendance(request):
    s = Sem1Students.objects.all()
    if request.method == "POST":
        if request.POST.getlist("present") or request.POST.getlist("absent"):
            subject = request.POST.get("subject")
            for p in request.POST.getlist("present"):
                Sem1Attendance.objects.create(
                    roll=p,
                    semester=1,
                    subject=subject,
                    status="Present",
                )
            for a in request.POST.getlist("absent"):
                Sem1Attendance.objects.create(
                    roll=a,
                    semester=1,
                    subject=subject,
                    status="Absent",
                )
            messages.success(request, "Attendance saved successfully!")
            return redirect('/staff/attendance/sem1')
        else:
            messages.error(request, "No data to save, try again!")
            return redirect('/staff/attendance/sem1')
    return render(request, 'staff/attendance/sem01.html', {'s': s})


# semester 2 attendance view
@login_required
def sem2Attendance(request):
    s = Sem2Students.objects.all()
    if request.method == "POST":
        if request.POST.getlist("present") or request.POST.getlist("absent"):
            subject = request.POST.get("subject")
            for p in request.POST.getlist("present"):
                Sem2Attendance.objects.create(
                    roll=p,
                    semester=2,
                    subject=subject,
                    status="Present",
                )
            for a in request.POST.getlist("absent"):
                Sem2Attendance.objects.create(
                    roll=a,
                    semester=2,
                    subject=subject,
                    status="Absent",
                )
            messages.success(request, "Attendance saved successfully!")
            return redirect('/staff/attendance/sem2')
        else:
            messages.error(request, "No data to save, try again!")
            return redirect('/staff/attendance/sem2')
    return render(request, 'staff/attendance/sem02.html', {'s': s})


# semester 3 attendance view
@login_required
def sem3Attendance(request):
    s = Sem3Students.objects.all()
    if request.method == "POST":
        if request.POST.getlist("present") or request.POST.getlist("absent"):
            subject = request.POST.get("subject")
            for p in request.POST.getlist("present"):
                Sem3Attendance.objects.create(
                    roll=p,
                    semester=3,
                    subject=subject,
                    status="Present",
                )
            for a in request.POST.getlist("absent"):
                Sem3Attendance.objects.create(
                    roll=a,
                    semester=3,
                    subject=subject,
                    status="Absent",
                )
            messages.success(request, "Attendance saved successfully!")
            return redirect('/staff/attendance/sem3')
        else:
            messages.error(request, "No data to save, try again!")
            return redirect('/staff/attendance/sem3')
    return render(request, 'staff/attendance/sem03.html', {'s': s})


# semester 4 attendance view
@login_required
def sem4Attendance(request):
    s = Sem4Students.objects.all()
    if request.method == "POST":
        if request.POST.getlist("present") or request.POST.getlist("absent"):
            subject = request.POST.get("subject")
            for p in request.POST.getlist("present"):
                Sem4Attendance.objects.create(
                    roll=p,
                    semester=4,
                    subject=subject,
                    status="Present",
                )
            for a in request.POST.getlist("absent"):
                Sem4Attendance.objects.create(
                    roll=a,
                    semester=4,
                    subject=subject,
                    status="Absent",
                )
            messages.success(request, "Attendance saved successfully!")
            return redirect('/staff/attendance/sem4')
        else:
            messages.error(request, "No data to save, try again!")
            return redirect('/staff/attendance/sem4')
    return render(request, 'staff/attendance/sem04.html', {'s': s})


# semester 5 attendance view


@login_required
def sem5Attendance(request):
    s = Sem5Students.objects.all()
    if request.method == "POST":
        if request.POST.getlist("present") or request.POST.getlist("absent"):
            subject = request.POST.get("subject")
            for p in request.POST.getlist("present"):
                Sem5Attendance.objects.create(
                    roll=p,
                    semester=5,
                    subject=subject,
                    status="Present",
                )
            for a in request.POST.getlist("absent"):
                Sem5Attendance.objects.create(
                    roll=a,
                    semester=5,
                    subject=subject,
                    status="Absent",
                )
            messages.success(request, "Attendance saved successfully!")
            return redirect('/staff/attendance/sem5')
        else:
            messages.error(request, "No data to save, try again!")
            return redirect('/staff/attendance/sem5')
    return render(request, 'staff/attendance/sem05.html', {'s': s})


# semester 6 attendance view


@login_required
def sem6Attendance(request):
    s = Sem6Students.objects.all()
    if request.method == "POST":
        if request.POST.getlist("present") or request.POST.getlist("absent"):
            subject = request.POST.get("subject")
            for p in request.POST.getlist("present"):
                Sem6Attendance.objects.create(
                    roll=p,
                    semester=6,
                    subject=subject,
                    status="Present",
                )
            for a in request.POST.getlist("absent"):
                Sem6Attendance.objects.create(
                    roll=a,
                    semester=6,
                    subject=subject,
                    status="Absent",
                )
            messages.success(request, "Attendance saved successfully!")
            return redirect('/staff/attendance/sem6')
        else:
            messages.error(request, "No data to save, try again!")
            return redirect('/staff/attendance/sem6')
    return render(request, 'staff/attendance/sem06.html', {'s': s})


# --------------------------------------------------------------------


# student details upload home
@login_required
def uploadHome(request):
    return render(request, 'student/upload/upload-home.html')

# semester 1 upload view, bulk create for faster upload


@login_required
def uploadStudents1(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ext = os.path.splitext(uploaded_file.name)[-1].lower()
        if ext == '.csv':
            data_file = pd.read_csv(
                uploaded_file)
            data_file.fillna('-', inplace=True)
            semi_st = []
            for _, row in data_file.iterrows():
                semi_st.append(Sem1Students(
                    roll_no=row['Roll No'],
                    ern=row['ERN'],
                    name=row['Name'],
                    contact_no=row['Contact'],
                    email=row['Email'],
                    class_details=row['Class Details']
                )
                )
            Sem1Students.objects.bulk_create(semi_st)
            messages.success(request, 'Uploaded student details successfully!')
            return redirect('/students/details/1')
        else:
            messages.error(request, "Invalid file type. Please upload again.")
            return render(request, 'student/upload1.html')

    return render(request, "student/upload/upload1.html")

# semester 2 upload view, bulk create for faster upload


@login_required
def uploadStudents2(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ext = os.path.splitext(uploaded_file.name)[-1].lower()
        if ext == '.csv':
            data_file = pd.read_csv(
                uploaded_file)
            data_file.fillna('-', inplace=True)
            semi_st = []
            for _, row in data_file.iterrows():
                semi_st.append(Sem2Students(
                    roll_no=row['Roll No'],
                    ern=row['ERN'],
                    name=row['Name'],
                    contact_no=row['Contact'],
                    email=row['Email'],
                    class_details=row['Class Details']
                )
                )
            Sem2Students.objects.bulk_create(semi_st)
            messages.success(request, 'Uploaded student details successfully!')
            return redirect('/students/details/2')
        else:
            messages.error(request, "Invalid file type. Please upload again.")
            return render(request, 'student/upload2.html')

    return render(request, "student/upload/upload2.html")

# semester 3 upload view, bulk create for faster upload


@login_required
def uploadStudents3(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ext = os.path.splitext(uploaded_file.name)[-1].lower()
        if ext == '.csv':
            data_file = pd.read_csv(
                uploaded_file)
            data_file.fillna('-', inplace=True)
            semi_st = []
            for _, row in data_file.iterrows():
                semi_st.append(Sem3Students(
                    roll_no=row['Roll No'],
                    ern=row['ERN'],
                    name=row['Name'],
                    contact_no=row['Contact'],
                    email=row['Email'],
                    class_details=row['Class Details']
                )
                )
            Sem3Students.objects.bulk_create(semi_st)
            messages.success(request, 'Uploaded student details successfully!')
            return redirect('/students/details/3')
        else:
            messages.error(request, "Invalid file type. Please upload again.")
            return render(request, 'student/upload3.html')

    return render(request, "student/upload/upload3.html")

# semester 4 upload view, bulk create for faster upload


@login_required
def uploadStudents4(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ext = os.path.splitext(uploaded_file.name)[-1].lower()
        if ext == '.csv':
            data_file = pd.read_csv(
                uploaded_file)
            data_file.fillna('-', inplace=True)
            semi_st = []
            for _, row in data_file.iterrows():
                semi_st.append(Sem4Students(
                    roll_no=row['Roll No'],
                    ern=row['ERN'],
                    name=row['Name'],
                    contact_no=row['Contact'],
                    email=row['Email'],
                    class_details=row['Class Details']
                )
                )
            Sem4Students.objects.bulk_create(semi_st)
            messages.success(request, 'Uploaded student details successfully!')
            return redirect('/students/details/4')
        else:
            messages.error(request, "Invalid file type. Please upload again.")
            return render(request, 'student/upload4.html')

    return render(request, "student/upload/upload4.html")

# semester 5 upload view, bulk create for faster upload


@login_required
def uploadStudents5(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ext = os.path.splitext(uploaded_file.name)[-1].lower()
        if ext == '.csv':
            data_file = pd.read_csv(
                uploaded_file)
            data_file.fillna('-', inplace=True)
            semi_st = []
            for _, row in data_file.iterrows():
                semi_st.append(Sem5Students(
                    roll_no=row['Roll No'],
                    ern=row['ERN'],
                    name=row['Name'],
                    contact_no=row['Contact'],
                    email=row['Email'],
                    class_details=row['Class Details']
                )
                )
            Sem5Students.objects.bulk_create(semi_st)
            messages.success(request, 'Uploaded student details successfully!')
            return redirect('/students/details/5')
        else:
            messages.error(request, "Invalid file type. Please upload again.")
            return render(request, 'student/upload5.html')

    return render(request, "student/upload/upload5.html")

# semester 6 upload view, bulk create for faster upload


@login_required
def uploadStudents6(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ext = os.path.splitext(uploaded_file.name)[-1].lower()
        if ext == '.csv':
            data_file = pd.read_csv(
                uploaded_file)
            data_file.fillna('-', inplace=True)
            semi_st = []
            for _, row in data_file.iterrows():
                semi_st.append(Sem6Students(
                    roll_no=row['Roll No'],
                    ern=row['ERN'],
                    name=row['Name'],
                    contact_no=row['Contact'],
                    email=row['Email'],
                    class_details=row['Class Details']
                )
                )
            Sem6Students.objects.bulk_create(semi_st)
            messages.success(request, 'Uploaded student details successfully!')
            return redirect('/students/details/6')
        else:
            messages.error(request, "Invalid file type. Please upload again.")
            return render(request, 'student/upload6.html')

    return render(request, "student/upload/upload6.html")


# ---------------------------------------------------------------

# view details home
@login_required
def studentsHome(request):
    return render(request, "student/student-home.html")

# sem 1 details


@login_required
def students1(request):
    std = Sem1Students.objects.all()
    context = {'stds': std}
    return render(request, "student/students1.html", context)


@login_required
def delete_student1(request, st_id1):
    record = Sem1Students.objects.get(pk=st_id1).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/students/details/1')


# sem 2 details
@login_required
def students2(request):
    std = Sem2Students.objects.all()
    context = {'stds': std}
    return render(request, "student/students2.html", context)


@login_required
def delete_student2(request, st_id2):
    record = Sem2Students.objects.get(pk=st_id2).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/students/details/2')

# sem 3 details


@login_required
def students3(request):
    std = Sem3Students.objects.all()
    context = {'stds': std}
    return render(request, "student/students3.html", context)


@login_required
def delete_student3(request, st_id3):
    record = Sem3Students.objects.get(pk=st_id3).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/students/details/3')

# sem 4 details


@login_required
def students4(request):
    std = Sem4Students.objects.all()
    context = {'stds': std}
    return render(request, "student/students4.html", context)


@login_required
def delete_student4(request, st_id4):
    record = Sem4Students.objects.get(pk=st_id4).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/students/details/4')

# sem 5 details


@login_required
def students5(request):
    std = Sem5Students.objects.all()
    context = {'stds': std}
    return render(request, "student/students5.html", context)


@login_required
def delete_student5(request, st_id5):
    record = Sem5Students.objects.get(pk=st_id5).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/students/details/5')

# sem 6 details


@login_required
def students6(request):
    std = Sem6Students.objects.all()
    context = {'stds': std}
    return render(request, "student/students6.html", context)


@login_required
def delete_student6(request, st_id6):
    record = Sem6Students.objects.get(pk=st_id6).delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('/students/details/6')

# -----------------------------------------------------------

# Student details update


@login_required
def update_view1(request, st_id1):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = Sem1Students.objects.get(pk=st_id1)

    # pass the object as instance in form
    form = Sem1StdUpdateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/students/details/1')

    # add form dictionary to context
    context["form"] = form

    return render(request, "student/update/update.html", context)


@login_required
def update_view2(request, st_id2):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = Sem2Students.objects.get(pk=st_id2)

    # pass the object as instance in form
    form = Sem2StdUpdateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/students/details/2')

    # add form dictionary to context
    context["form"] = form

    return render(request, "student/update/update.html", context)


@login_required
def update_view3(request, st_id3):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = Sem3Students.objects.get(pk=st_id3)

    # pass the object as instance in form
    form = Sem3StdUpdateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/students/details/3')

    # add form dictionary to context
    context["form"] = form

    return render(request, "student/update/update.html", context)


@login_required
def update_view4(request, st_id4):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = Sem4Students.objects.get(pk=st_id4)

    # pass the object as instance in form
    form = Sem4StdUpdateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/students/details/4')

    # add form dictionary to context
    context["form"] = form

    return render(request, "student/update/update.html", context)


@login_required
def update_view5(request, st_id5):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = Sem5Students.objects.get(pk=st_id5)

    # pass the object as instance in form
    form = Sem5StdUpdateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/students/details/5')

    # add form dictionary to context
    context["form"] = form

    return render(request, "student/update/update.html", context)


@login_required
def update_view6(request, st_id6):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = Sem6Students.objects.get(pk=st_id6)

    # pass the object as instance in form
    form = Sem6StdUpdateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/students/details/6')

    # add form dictionary to context
    context["form"] = form

    return render(request, "student/update/update.html", context)
