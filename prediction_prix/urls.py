from django.urls import path
from  . import views


urlpatterns =[
   # path('',views.index,name='index'),
    path('commerce/',views.commerce,name='commerce'),
    path('predict/',views.predire,name='predire')
    
]
