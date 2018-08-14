from django.shortcuts import render
from .models import Thegun
# Create your views here.
def get_name(req):
    data = Thegun.objects.all()
    data1 = Thegun.objects.filter(name__contains="m")
    data2 = Thegun.objects.filter(capacity__in=[35,30,15])
    data3 = Thegun.objects.filter(capacity__gt=30)
    data4 = Thegun.objects.filter(date__year=2018)
    return render(req,"hw8_14copy.html",context={"key":data,"key1":data1,"key2":data2,"key3":data3,
                                                   "key4":data4,})