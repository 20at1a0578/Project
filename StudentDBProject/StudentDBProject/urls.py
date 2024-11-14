from django.contrib import admin
from django.urls import path
from django.urls import re_path
from StudentDBApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studenthomepage/', views.student_homepage),

    path('studentinputview2/', views.studentinputview2),

    path('studentinputview/',views.studentinputview),
    path('studinputverifyview/',views.studentinputverifyview),
    path('studentloginpage/', views.studentloginpageview),
    path('studentloginverifypage/', views.studentloginverifypageview),
    path('studentfeedback/', views.feedbackview),
]