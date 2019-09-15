from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Grievant(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE)
    Registeration = models.IntegerField(default=0000)
    Room = models.CharField(max_length=50)
    Hostel = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student.username


class Complaint(models.Model):
    grievant = models.ForeignKey('complaints_app.Grievant',on_delete=models.CASCADE,related_name='person')
    department_choice = [('Pl','Plumbing'),('Ca','Carpentry'),('El','Electricity')]
    department = models.CharField(choices=department_choice,max_length=2,default='Pl')
    text = models.TextField()
    heading = models.CharField(max_length=200,blank=True,null=True)
    media = models.ImageField(upload_to='media/')
    created_date = models.DateTimeField(default=timezone.now())
    status_choices = [('D','Done'),('P','Pending'),('N','Not Accepted')]
    status = models.CharField(choices=status_choices,max_length=1,default='N')

    class Meta():
        verbose_name_plural = 'Complaints'

    def change_status(self,choice):
        self.status = choice
        self.save()

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("complaint_detail",kwargs={'pk':self.pk})

class Department(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department_choice = [('Pl','Plumbing'),('Ca','Carpentry'),('El','Electricity')]
    name = models.CharField(choices=department_choice,max_length=2,default='Pl')

    def __str__(self):
        return self.name
