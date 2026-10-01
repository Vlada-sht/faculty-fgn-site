from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('programs/', views.programs, name='programs'),
    path('programs/<int:id>/', views.program_detail, name='program_detail'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:id>/', views.department_detail, name='department_detail'),
    path('admission/', views.admission, name='admission'),
    path('exchange/', views.exchange, name='exchange'),
]