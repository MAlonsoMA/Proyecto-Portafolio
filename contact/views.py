from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from .models import Location
import folium
from folium.plugins import FastMarkerCluster
from backgrounds.models import BackgroundImage

def contact(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactForm()
    
    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            # Enviar el correo electrónico
            email = EmailMessage(
                'Proyecto Porfolio',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['manuelalonsoweb@gmail.com'],
                reply_to=[email],
            )
            
            try:
                email.send()
                # Está todo OK
                return redirect(reverse('contact')+'?ok')
            except:
                # Ha habido un error y retorno a ERROR
                return redirect(reverse('contact')+'?error')
    
    #TRATAMIENTO DEL MAPA
    # Recupero todas las localizaciones
    locations = Location.objects.all()

    # Defino el mapa
    initialMap = folium.Map(location=[39.4873809,-0.9086], zoom_start=9, maxheight=1000)

    # Creamos el Clustering de los marcadores
    latitudes = [location.lat for location in locations]
    longitudes = [location.lng for location in locations]
    popups = [location.name for location in locations]
    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)

    #incorporacion textos imagen fondo
    backgrounds=BackgroundImage.objects.all()

    return render(request, 'contact/contact.html', {'form':contact_form,'map':initialMap._repr_html_(), 'locations':locations, 'backgrounds':backgrounds})