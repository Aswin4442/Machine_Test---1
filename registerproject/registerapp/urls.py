from django.urls import path
from .import views

urlpatterns = [
    path('output/',views.output,name='output'),
    path('view/',views.view,name='view'),
    path('downlod/<int:pk>/',views.dnld_img,name='dnld_img'),
]