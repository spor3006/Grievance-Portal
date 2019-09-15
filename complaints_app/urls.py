from . import views
from django.urls import path

urlpatterns = [
    path('',views.AboutView.as_view(),name='about'),
    path('login/',views.userlogin,name='login'),
    path('usercomplaintlist/<int:pk>/',views.ComplaintListUserView.as_view(),name='complaint_list_user'),
    path('register/',views.register,name='register'),
    path('post/<int:pk>/',views.ComplaintDetailView.as_view(),name='complaint_detail'),
    path('post/new/',views.CreateComplaintView.as_view(),name='create_complaint'),
    path('post/<int:pk>/edit/',views.UpdateComplaintView.as_view(),name='update_complaint'),
    path('post/<int:pk>/remove/',views.DeleteComplaintView.as_view(),name='remove_complaint'),
]
