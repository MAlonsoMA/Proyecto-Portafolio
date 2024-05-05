from django.shortcuts import render
from django.db.models import Q
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})

# Detalle del project
def detail_project(request, project_id):
    detail=Project.objects.get(id=project_id)
    return render(request, 'portfolio/detail.html', {'detail':detail})

""" def detail_project(request, project_id):
    detail=get_object_or_404(Project,id=project_id)
    print(detail)
    return render(request, 'portfolio/detail.html', {'detail':detail}) """

#filtrado por busqueda
def search(request):
    queryset=request.GET.get("search")
    if queryset:
        projects=Project.objects.filter(
            Q(title__icontains=queryset) | 
            Q(description__icontains=queryset) |
            Q(detalle__icontains=queryset) |
            Q(pie__icontains=queryset) |
            Q(autor__icontains=queryset),
        ).distinct()
    else:
        projects={}
    return render(request,'portfolio/search.html',{'projects':projects,'queryset':queryset})