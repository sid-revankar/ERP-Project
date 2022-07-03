from django import forms
from .models import *


class Sem1AttendanceForm(forms.ModelForm):
    class Meta:
        model = Sem1Attendance
        fields = '__all__'

class Sem2AttendanceForm(forms.ModelForm):
    class Meta:
        model = Sem2Attendance
        fields = '__all__'

class Sem3AttendanceForm(forms.ModelForm):
    class Meta:
        model = Sem3Attendance
        fields = '__all__'

class Sem4AttendanceForm(forms.ModelForm):
    class Meta:
        model = Sem4Attendance
        fields = '__all__'

class Sem5AttendanceForm(forms.ModelForm):
    class Meta:
        model = Sem5Attendance
        fields = '__all__'

class Sem6AttendanceForm(forms.ModelForm):
    class Meta:
        model = Sem6Attendance
        fields = '__all__'

class Sem1StdUpdateForm(forms.ModelForm):
    class Meta:
        model = Sem1Students
        fields = '__all__'

class Sem2StdUpdateForm(forms.ModelForm):
    class Meta:
        model = Sem2Students
        fields = '__all__'

class Sem3StdUpdateForm(forms.ModelForm):
    class Meta:
        model = Sem3Students
        fields = '__all__'

class Sem4StdUpdateForm(forms.ModelForm):
    class Meta:
        model = Sem4Students
        fields = '__all__'

class Sem5StdUpdateForm(forms.ModelForm):
    class Meta:
        model = Sem5Students
        fields = '__all__'

class Sem6StdUpdateForm(forms.ModelForm):
    class Meta:
        model = Sem6Students
        fields = '__all__'        