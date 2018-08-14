from django.conf.urls import url
from .views import my_carts
urlpatterns = [
    url(r"train$",my_carts)
]