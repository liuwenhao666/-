from django.shortcuts import render
from .models import Firecart
# Create your views here.
def my_carts(req):
    data = Firecart.objects.filter(speed__lt=300).order_by("speed")
    result = {
        "tltle":"huocart",
        "carts":data
    }
    return render(req,"trina.html",result)