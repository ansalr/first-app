from django.shortcuts import render
from.models import Destination

# Create your views here.

def index (request):

    dest1 = Destination()
    dest1.name = "hawai"
    dest1.desc = " beach resort"
    dest1.price = 666

    dest2 = Destination()
    dest2.name = "Shahara"
    dest2.desc = " sunny light "
    dest2.price = 696

    dest3 = Destination()
    dest3.name = "red bridge"
    dest3.desc = " hanging pridge"
    dest3.price = 969
    return render(request,'index.html',{'dest1': dest1 ,'dest2' : dest2 ,'dest3':dest3 })
