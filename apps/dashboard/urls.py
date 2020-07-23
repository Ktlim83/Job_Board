from django.urls import path
from apps.dashboard.models import *
from . import views

urlpatterns = [
     # local8000/jobs
    path('', views.index),
    # local8000/jobs/new
    path('new',views.new),
    # local8000/jobs/add_job
    path('add_job',views.add_job),
    # local8000/jobs/<job_id>/edit
    path('<int:job_id>/edit', views.edit),
    # local8000/jobs/<job_id>/update
    path('<int:job_id>/update', views.update),
    # local8000/jobs/<job_id>/delete
    path('<int:job_id>/delete', views.delete),
    # local8000/jobs/<jobs_id>
    path('<int:job_id>',views.view_job),
    path('<int:job_id>/add', views.accept),
    path('<int:job_id>/giveup', views.giveup),
    
    
]
