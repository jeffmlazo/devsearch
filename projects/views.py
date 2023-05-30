from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': "1",
        'title': "Ecommerce Website",
        'description': "Fully functional ecommerce website"
    },
    {
        'id': "2",
        'title': "Porfolio Website",
        'description': "This was a project where I built out my portfolio"
    },
    {
        'id': "3",
        'title': "Social Network",
        'description': "Awesome open source project I am still woking on"
    },
]


def projects(request):
    page = 'Hello, you are on the projects page'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    context = {'project': projectObj}
    return render(request, "projects/single-project.html", context)
