from django.shortcuts import render
from .models import Pro_language
# Create your views here.
def get_data(req):
    data = Pro_language.objects.all()
    return render(req,"homework_8_13.html",context={"mydata":data})