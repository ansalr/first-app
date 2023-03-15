from django.shortcuts import render
from.models import Destination

# Create your views here.

def index (request):

    dest1 = Destination()
    dest1.name = "hawai"
    dest1.desc = " beach resort"
    dest1.img = "destination_1.jpg"    
    dest1.price = 666

    dest2 = Destination()
    dest2.name = "Shahara"
    dest2.desc = " sunny light "
    dest2.img = "destination_2.jpg" 
    dest2.price = 696

    dest3 = Destination()
    dest3.name = "red bridge"
    dest3.desc = " hanging pridge"
    dest3.img = "destination_3.jpg" 
    dest3.price = 969

    dests = [dest1,dest2,dest3]
    return render(request,'index.html',{'dests': dests })
