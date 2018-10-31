from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.BeersHomeView.as_view(), name='totalbeers'),
    # url(r'^detail/(?P<beerid>\d+)', views.DetailView.as_view(), name='beer_detail'),
]