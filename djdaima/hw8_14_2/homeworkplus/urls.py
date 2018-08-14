from django.conf.urls import url
from .views import get_name

urlpatterns = [
    url(r'^3$',get_name)
]