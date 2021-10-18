from django.urls import path

from . import views
app_name = 'api'

urlpatterns = [
    path('api/v1/calculate', views.calculate1, name='api/v1/calculate'),


]
