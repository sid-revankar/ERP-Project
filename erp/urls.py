from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),
    path('', include('staff.staff_urls')),
    path('', include('students.student_urls')),
    path('', include('results.results_urls')),
]
