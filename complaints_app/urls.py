from . import views
from django.urls import path

urlpatterns = [
    path('',views.AboutView.as_view(),name='about'),
    path('login/',views.userlogin,name='login'),
    path('register/',views.register,name='register')
]
