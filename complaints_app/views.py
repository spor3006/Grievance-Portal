from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from complaints_app.models import Grievant,Complaint,Department,User
from django.utils import timezone
from complaints_app.forms import ComplaintForm,UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
# Create your views here.

class AboutView(TemplateView):
    template_name = 'complaints_app/about.html'

class ComplaintDetailView(DetailView):
    model = Complaint


class ComplaintListUserView(ListView):
    model = Complaint

    def get_queryset(self):
        grievant = Grievant.objects.get(student = self.request.user)
        return Complaint.objects.filter(grievant = grievant)



class CreateComplaintView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'complaints_app/complaint_detail.html'

    form_class = ComplaintForm

    model = Complaint

class UpdateComplaintView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'complaints_app/complaint_detail.html'

    form_class = ComplaintForm

    model = Complaint

class DeleteComplaintView(LoginRequiredMixin,DeleteView):
    model = Complaint
    success_url = reverse_lazy('complaints_list')



def register(request):
    if request.method == 'POST':
        if Grievant.objects.filter(Registeration=request.POST['reg_num']).count() >0:
            response = {}
            response['error'] = 'This Registeration Number already exists'
            return render(request,'registeration/signup.html',response)
        username = request.POST['username']
        password = request.POST['password']
        reg_num = request.POST['reg_num']
        password2 = request.POST['password2']
        room_num = request.POST['room_num']
        hostel = request.POST['hostel']
        if password != password2:
            return render(request,'registeration/signup.html', {'error' : 'Passwords dont match'})
        student = User.objects.create(username = username, password=make_password(password))
        grievant = Grievant.objects.create(student = student ,Registeration=reg_num,Room=room_num,Hostel=hostel)
        grievant.save()
        return redirect('/')
    return render(request, 'registeration/signup.html', None)


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username+" "+password)
        user = authenticate(username= username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('about'))
            else:
                return HttpResponse('Your account was inactive')
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request,'registeration/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('about'))
