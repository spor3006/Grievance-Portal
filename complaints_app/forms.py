from django import forms
from complaints_app.models import Department,Complaint
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class ComplaintForm(forms.ModelForm):

    class Meta():
        model = Complaint
        fields = ('grievant','department','heading','text','media')

class UserForm(UserCreationForm):

    reg_num = forms.IntegerField()
    room_num = forms.CharField(max_length=50)
    hostel = forms.CharField(max_length=100)

    class Meta():
        model = User
        fields = ['username','reg_num','room_num','hostel','password1', 'password2']
