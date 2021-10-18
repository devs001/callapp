from django.urls import path

from . import views
app_name='customer'

urlpatterns = [
    path('add_data', views.import_data, name='add_data'),
    path('vi/calculate', views.calculate1, name='vi'),


]
