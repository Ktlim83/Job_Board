from django.db import models
from apps.log_reg_app.models import *


class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}

        if len(postData['title']) < 3:
            errors['title'] = "a job must consist of atleast 3 characters!."
        if postData['location'] == "":
            errors['location'] = "A location must be provided!"

        return errors


class Job(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    location = models.CharField(max_length = 255)
    user_posted_job = models.ForeignKey(User, related_name='posted_job', on_delete=models.CASCADE)
    user_with_job = models.ManyToManyField(User, related_name='with_job')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    
    objects = JobManager()

    def __str__(self):
        return f"{self.id} {self.title}"
    
    
    
 

    
    
    

