from django.shortcuts import render

# Create your views here.
def projects_list(request):
    return render(request, 'content/projects_list.html')


#create,edit, delete... Project
# localhost/content/projects
# localhost/content/new
# localhost/content/edit_id