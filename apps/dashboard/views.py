from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.log_reg_app.models import *
from apps.dashboard import *
from .models import *



# LOADS DASHBOARD 
def index(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        "all_jobs": Job.objects.all(),

    }
    
    return render(request, "main/index.html", context)


# LOADS NEW JOB PAGE 
def new(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        "all_jobs": Job.objects.all(),
    }
    return render(request, "main/new.html", context)


# ADDS NEW JOB 
def add_job(request):
    errors = Job.objects.job_validator(request.POST)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags='fieldErrors')
        return redirect('/jobs/new')
    
    else:
        user = User.objects.get(id=request.session["user_id"])
        job = Job.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            location = request.POST['location'],
            user_posted_job = user
        )
        return redirect('/jobs')
    
# LOADS EDIT PAGE
def edit(request, job_id):
    one_job = Job.objects.get(id=job_id)
    context = {
         'job' : one_job
    }
    return render(request, "main/edit.html", context)

# UPDATES JOB 
def update(request, job_id):
    errors = Job.objects.job_validator(request.POST)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags='fieldErrors')
        return redirect(f'/jobs/{job_id}/edit')
    
    else:
        update_job = Job.objects.get(id=job_id)
        update_job.title = request.POST['title']
        update_job.description = request.POST['description']
        update_job.location = request.POST['location']
        update_job.save()
        
        return redirect('/jobs')


# DELETES JOB 
def delete(request, job_id):
    delete_job = Job.objects.get(id=job_id)
    delete_job.delete()
    return redirect('/jobs')  


# VIEWS JOB 
def view_job(request, job_id):
    one_job = Job.objects.get(id=job_id)
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'job' : one_job,
    }
    return render(request, "main/view.html", context)  
        


# DELETE AN uSER 
def remove_user(request, user_id):
    del_user = User.objects.get(id=user_id)
    del_user.delete()
    return redirect('/')


# ADDS JOB TO USER 
def accept(request, job_id):
        job = Job.objects.get(id=job_id)
        user = User.objects.get(id=request.session["user_id"])
        user.with_job.add(job)
        
        
        return redirect('/jobs/')
    
    
# REMOVE JOB FROM USER 
def giveup(request, job_id):
    user = User.objects.get(id=request.session["user_id"])
    job = Job.objects.get(id=job_id)
    user.with_job.remove(job)
    

    return redirect('/jobs/')

# DELETES JOB 
def delete(request, job_id):
    delete_job = Job.objects.get(id=job_id)
    delete_job.delete()
    return redirect('/jobs')  
    














