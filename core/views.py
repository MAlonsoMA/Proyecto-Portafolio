from django.shortcuts import render
from backgrounds.models import BackgroundImage

# Create your views here.
def home(request):
    backgrounds=BackgroundImage.objects.all()
    return render(request, 'core/home.html',{'backgrounds':backgrounds})
