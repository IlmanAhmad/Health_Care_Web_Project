from . import views
from django.urls import path


app_name = 'doc'

urlpatterns = [
    path('', views.index, name='home'),
    path('handlelogin/', views.handlelogin, name = 'handlelogin'),
    path('logout/', views.handlelogout, name = 'handlelogout'),
    path('patient/', views.patient, name = 'patient'),
    path('search/', views.search, name = 'search')
]