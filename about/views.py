from django.shortcuts import render
from .models import Course, Skill
from backgrounds.models import BackgroundImage

# Create your views here.
def about(request):
    courses = Course.objects.all()
    skills = Skill.objects.all()
    backgrounds=BackgroundImage.objects.all()

    return render(request, 'about/about.html', {'courses':courses, 'skills':skills,'backgrounds':backgrounds})