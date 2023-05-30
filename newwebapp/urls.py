from django.urls import path
from newwebapp import views

urlpatterns = [

    path('newhomepage/',views.newhomepage,name="newhomepage")


]

