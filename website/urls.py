from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('simple_view/', views.simple_view, name='simple_view'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.RecordView.as_view(), name='record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record')
]