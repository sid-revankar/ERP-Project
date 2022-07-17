from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# IMPORT FORMS
from .forms import Sem1IaForm, Sem2IaForm, Sem3IaForm, Sem4IaForm

# PANDAS IMPORT AND NUMPY IMPORT
import pandas as pd

# IMPORT IN-BUILT MODULES
import os

# MODEL IMPORT
from .models import oddSemResult, evenSemResult, IaSem1, IaSem2, IaSem3, IaSem4
from students.models import Sem1Students, Sem2Students, Sem3Students, Sem4Students

# Displays the table contents on the ODD-Data-Table


def oddResult(request):
    dis = oddSemResult.objects.all()
    context = {
        'dis': dis
    }

    return render(request, "results/odd-display.html", context)

# Displays the table contents on the EVEN-Data-Table


def evenResult(request):
    dis = evenSemResult.objects.all()
    context = {
        'dis': dis
    }
    return render(request, "results/even-display.html", context)


'''def viewReport(request):
    labels = []
    data = []

    rep = File.objects.order_by('-reg_no')[:50]
    for r in rep:
        labels.append(r.student_name)
        data.append(r.ex_total)

    context = {
        'labels': labels,
        'data': data,
    }

    return render(request, 'results/viewreport.html', context)'''

# Uploading CSV for ODD-SEM Results


@login_required
def oddSemUpload(request):
    if request.method == "POST":
        csv_file = request.FILES['upload']
        ext = os.path.splitext(csv_file.name)[-1].lower()
        if ext == '.csv':
            reader = pd.read_csv(csv_file)
            reader.fillna('-', inplace=True)
            result = []
            for _, row in reader.iterrows():
                result.append(oddSemResult(
                    reg_no=row['Reg No'],
                    student_name=row['Student Name'],
                    sem=row['Sem'],
                    ex1=row['EX-1'],
                    ex2=row['EX-2'],
                    ex3=row['EX-3'],
                    ex4=row['EX-4'],
                    ex5=row['EX-5'],
                    ex6=row['EX-6'],
                    ex7=row['EX-7'],
                    ex_total=row['Ex-Total'],
                    ia1=row['IA-1'],
                    ia2=row['IA-2'],
                    ia3=row['IA-3'],
                    ia4=row['IA-4'],
                    ia5=row['IA-5'],
                    ia6=row['IA-6'],
                    ia7=row['IA-7'],
                    ia_total=row['IA=Total'],
                    total=row['Total'],
                    result=row['Result'],
                    kx1=row['KX-1'],
                    ki1=row['KI-1'],
                    k_result=row['K-Result']
                ))

            oddSemResult.objects.bulk_create(result)
            messages.success(request, "CSV Uploaded Successfully")
        else:
            messages.error(request, "Invalid File Format, Please Try Again!")
    return render(request, "results/oddResult.html")


@login_required
# Uploading CSV for EVEN-SEM Results
def evenSemUpload(request):
    if request.method == "POST":
        csv_file = request.FILES['upload']
        ext = os.path.splitext(csv_file.name)[-1].lower()
        if ext == '.csv':
            reader = pd.read_csv(csv_file)
            reader.fillna('', inplace=True)
            result = []
            for _, row in reader.iterrows():
                result.append(evenSemResult(
                    reg_no=row['Reg No'],
                    student_name=row['Student Name'],
                    sem=row['Sem'],
                    ex1=row['EX-1'],
                    ex2=row['EX-2'],
                    ex3=row['EX-3'],
                    ex4=row['EX-4'],
                    ex5=row['EX-5'],
                    ex6=row['EX-6'],
                    ex7=row['EX-7'],
                    ex_total=row['Ex-Total'],
                    ia1=row['IA-1'],
                    ia2=row['IA-2'],
                    ia3=row['IA-3'],
                    ia4=row['IA-4'],
                    ia5=row['IA-5'],
                    ia6=row['IA-6'],
                    ia7=row['IA-7'],
                    ia_total=row['IA=Total'],
                    total=row['Total'],
                    result=row['Result'],
                    kx1=row['KX-1'],
                    ki1=row['KI-1'],
                    k_result=row['K-Result']
                ))

            evenSemResult.objects.bulk_create(result)
            messages.success(request, "CSV Uploaded Successfully!")
        else:
            messages.error(request, "Invalid File Format, Please Try Again!")
    return render(request, "results/evenResult.html")

@login_required
def evenResultDelete(request):
    if request.user.is_superuser:
        evenSemResult.objects.all().delete()
        messages.success(request, 'All even semester results deleted!')
        return redirect('/results/view/even/')

@login_required
def oddResultDelete(request):
    if request.user.is_superuser:
        oddSemResult.objects.all().delete()
        messages.success(request, 'All odd semester results deleted!')
        return redirect('/results/view/odd/')


@login_required
def iaHome(request):
    return render(request, 'ia/iahome.html')


@login_required
def iaSem1Upload(request):
    if request.method == 'POST':
        form1 = Sem1IaForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Internal Marks added successfully!")
            return redirect('/results/ia/sem1')
    else:
        form1 = Sem1IaForm()
    return render(request, 'ia/sem1.html', {'form1': form1})


@login_required
def iaSem2Upload(request):
    if request.method == 'POST':
        form2 = Sem2IaForm(request.POST)
        if form2.is_valid():
            form2.save()
            messages.success(request, "Internal Marks added successfully!")
            return redirect('/results/ia/sem2')
    else:
        form2 = Sem2IaForm()
    return render(request, 'ia/sem2.html', {'form2': form2})


@login_required
def iaSem3Upload(request):
    if request.method == 'POST':
        form3 = Sem3IaForm(request.POST)
        if form3.is_valid():
            form3.save()
            messages.success(request, "Internal Marks added successfully!")
            return redirect('/results/ia/sem3')
    else:
        form3 = Sem3IaForm()
    return render(request, 'ia/sem3.html', {'form3': form3})


@login_required
def iaSem4Upload(request):
    if request.method == 'POST':
        form4 = Sem4IaForm(request.POST)
        if form4.is_valid():
            form4.save()
            messages.success(request, "Internal Marks added successfully!")
            return redirect('/results/ia/sem4')
    else:
        form4 = Sem4IaForm()
    return render(request, 'ia/sem4.html', {'form4': form4})

just a fuckin test! where does this shit go?
