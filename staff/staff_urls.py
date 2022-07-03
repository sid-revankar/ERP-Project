from django.urls import path
from . import staff_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # user login urls
    path('login/', staff_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # end

    # homepage url
    path('', staff_views.home, name='homepage'),
    path('staff/', staff_views.staff_home, name='staff-home'),
    # end

    # timetable view and CRUD urls
    path('staff/time-table/', staff_views.display_tt, name='time_table'),
    path('staff/time-table/update/<tt_id>/',
         staff_views.update_record, name='update_tt'),
    path('staff/time-table/delete-tt/<tt_id>/',
         staff_views.delete_record, name='delete_tt'),
    # end

    # feedback url
    path('staff/feedback/', staff_views.view_feedback, name='view-feedback'),
    path('staff/feedback/delete/<f_id>',
         staff_views.delete_feedback, name='delete-feedback'),

    # attendance
    path('staff/attendance/', staff_views.attendance, name='attendance'),
    path('staff/attendance/sem1',
         staff_views.sem1Attendance, name='attendance-sem1'),
    path('staff/attendance/sem2',
         staff_views.sem2Attendance, name='attendance-sem2'),
    path('staff/attendance/sem3',
         staff_views.sem3Attendance, name='attendance-sem3'),
    path('staff/attendance/sem4',
         staff_views.sem4Attendance, name='attendance-sem4'),
    path('staff/attendance/sem5',
         staff_views.sem5Attendance, name='attendance-sem5'),
    path('staff/attendance/sem6',
         staff_views.sem6Attendance, name='attendance-sem6'),

    # student urls
    path('students/details', staff_views.studentsHome, name='students-home'),

    path('students/details/1', staff_views.students1, name='students1'),
    path('students/delete/1/<st_id1>', staff_views.delete_student1, name='del1'),
    
    path('students/details/2', staff_views.students2, name='students2'),
    path('students/delete/2/<st_id2>', staff_views.delete_student2, name='del2'),

    path('students/details/3', staff_views.students3, name='students3'),
    path('students/delete/3/<st_id3>', staff_views.delete_student3, name='del3'),

    path('students/details/4', staff_views.students4, name='students4'),
    path('students/delete/4/<st_id4>', staff_views.delete_student4, name='del4'),

    path('students/details/5', staff_views.students5, name='students5'),
    path('students/delete/5/<st_id5>', staff_views.delete_student5, name='del5'),

    path('students/details/6', staff_views.students6, name='students6'),
    path('students/delete/6/<st_id6>', staff_views.delete_student6, name='del6'),

    path('students/upload/', staff_views.uploadHome, name='upload-home'),
    path('students/upload/1', staff_views.uploadStudents1, name='upload1'),
    path('students/upload/2', staff_views.uploadStudents2, name='upload2'),
    path('students/upload/3', staff_views.uploadStudents3, name='upload3'),
    path('students/upload/4', staff_views.uploadStudents4, name='upload4'),
    path('students/upload/5', staff_views.uploadStudents5, name='upload5'),
    path('students/upload/6', staff_views.uploadStudents6, name='upload6'),
    
    #student upadte URL's

    path('students/update/1/<st_id1>', staff_views.update_view1, name='update1'),
    path('students/update/2/<st_id2>', staff_views.update_view2, name='update2'),
    path('students/update/3/<st_id3>', staff_views.update_view3, name='update3'),
    path('students/update/4/<st_id4>', staff_views.update_view4, name='update4'),
    path('students/update/5/<st_id5>', staff_views.update_view5, name='update5'),
    path('students/update/6/<st_id6>', staff_views.update_view6, name='update6'),
    # end
]
