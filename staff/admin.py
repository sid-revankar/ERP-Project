from django.contrib import admin
from .models import *
from students.models import *

from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import resources

# import export functionalities for all attendance models.


class Sem1AttendanceResource(resources.ModelResource):
    roll= Field()
    f_date = Field(attribute='date', column_name='date')

    class Meta:
        model = Sem1Attendance
        fields = ('roll', 'status', 'semester', 'subject', 'f_date')

    def dehydrate_roll(self, Sem1Attendance):
        return '%s' % (Sem1Attendance.roll)


class Attendance1Admin(ImportExportModelAdmin):
    resource_class = Sem1AttendanceResource


admin.site.register(Sem1Attendance, Attendance1Admin)


class Sem2AttendanceResource(resources.ModelResource):
    roll = Field()
    f_date = Field(attribute='date', column_name='date')

    class Meta:
        model = Sem2Attendance
        fields = ('roll', 'status', 'semester', 'subject', 'f_date')

    def dehydrate_roll(self, Sem2Attendance):
        return '%s' % (Sem2Attendance.roll)


class Attendance2Admin(ImportExportModelAdmin):
    resource_class = Sem2AttendanceResource


admin.site.register(Sem2Attendance, Attendance2Admin)


class Sem3AttendanceResource(resources.ModelResource):
    roll = Field()
    f_date = Field(attribute='date', column_name='date')

    class Meta:
        model = Sem3Attendance
        fields = ('roll', 'status', 'semester', 'subject', 'f_date')

    def dehydrate_roll(self, Sem3Attendance):
        return '%s' % (Sem3Attendance.roll)


class Attendance3Admin(ImportExportModelAdmin):
    resource_class = Sem3AttendanceResource


admin.site.register(Sem3Attendance, Attendance3Admin)


class Sem4AttendanceResource(resources.ModelResource):
    roll = Field()
    f_date = Field(attribute='date', column_name='date')

    class Meta:
        model = Sem4Attendance
        fields = ('roll', 'status', 'semester', 'subject', 'f_date')

    def dehydrate_roll(self, Sem4Attendance):
        return '%s' % (Sem4Attendance.roll)


class Attendance4Admin(ImportExportModelAdmin):
    resource_class = Sem4AttendanceResource


admin.site.register(Sem4Attendance, Attendance4Admin)


class Sem5AttendanceResource(resources.ModelResource):
    roll = Field()
    f_date = Field(attribute='date', column_name='date')

    class Meta:
        model = Sem5Attendance
        fields = ('roll', 'status', 'semester', 'subject', 'f_date')

    def dehydrate_roll(self, Sem5Attendance):
        return '%s' % (Sem5Attendance.roll)


class Attendance5Admin(ImportExportModelAdmin):
    resource_class = Sem5AttendanceResource


admin.site.register(Sem5Attendance, Attendance5Admin)


class Sem6AttendanceResource(resources.ModelResource):
    roll = Field()
    f_date = Field(attribute='date', column_name='date')

    class Meta:
        model = Sem6Attendance
        fields = ('roll', 'status', 'semester', 'subject', 'f_date')

    def dehydrate_roll(self, Sem6Attendance):
        return '%s' % (Sem6Attendance.roll)


class Attendance6Admin(ImportExportModelAdmin):
    resource_class = Sem6AttendanceResource


admin.site.register(Sem6Attendance, Attendance6Admin)


# student model admin registers

admin.site.register(Sem1Students)
admin.site.register(Sem2Students)
admin.site.register(Sem3Students)
admin.site.register(Sem4Students)
admin.site.register(Sem5Students)
admin.site.register(Sem6Students)
