from django.urls import path
from results import results_views as views


urlpatterns = [
    path('results/odd/', views.oddSemUpload, name="result-odd"),
    path('results/even/', views.evenSemUpload, name="result-even"),
    path('results/view/odd/', views.oddResult, name="odd-display"),
    path('results/view/even/', views.evenResult, name="even-display"),
    path('results/ia/', views.iaHome, name="ia-upload"),
    path('results/ia/sem1/', views.iaSem1Upload, name="iasem1-upload"),
    path('results/ia/sem2/', views.iaSem2Upload, name="iasem2-upload"),
    path('results/ia/sem3/', views.iaSem3Upload, name="iasem3-upload"),
    path('results/ia/sem4/', views.iaSem4Upload, name="iasem4-upload"),
    path('results/delete/even/', views.evenResultDelete, name="even-result-delete"),
    path('results/delete/odd/', views.oddResultDelete, name="odd-result-delete"),
    path('results/view/search', views.searchResult, name="result-search"),


]
