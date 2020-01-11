from django.db import models
from django.utils import timezone
from django.urls import reverse

class Manager(models.Model):
    name = models.CharField(max_length=100)
    team=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    comment=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    manager = models.ForeignKey(Manager, related_name='comments', on_delete=models.CASCADE)

    def json(self):
       return  [self.manager.name,self.date_posted.strftime("%Y-%m-%d %H:%M:%S"),self.comment]

    def get_absolute_url(self):
        #return reverse('cbv2:students',kwargs={'pk':self.pk})
        return reverse('feedback:home')


    def __str__(self):
        return self.comment