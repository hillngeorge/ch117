from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects_list, name="projects_list"), 
]


#create,edit, delete... Project
# localhost/content/projects
# localhost/content/new
# localhost/content/edit_id