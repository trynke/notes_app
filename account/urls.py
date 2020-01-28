from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='account/registration/logged_out.html'), name='logout'),
    url(r'^$', views.board, name='board'),
    url(r'^register/$', views.register, name='register'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
]
