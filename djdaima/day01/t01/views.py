from django.http import HttpResponse
from django.shortcuts import render
from .models import Engineer
# Create your views here.
def index(requeset):
    return HttpResponse("hello Django!!!")
# def my_html(req):
#     return render(req,"my_text.html")
def get_data(req):
    data = Engineer.objects.all()
    print(data)
    return render(req,"my_text.html",context={"my_data":data})