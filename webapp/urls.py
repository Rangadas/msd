from django.urls import path
from webapp import views

urlpatterns = [
path("homepage/",views.homepage,name="homepage"),
path("aboutpage/",views.aboutpage,name="aboutpage"),
path('productpage/<catg>/',views.productpage,name="productpage"),
path('moredetails/<int:dataid>/',views.moredetails,name="moredetails"),
path('contactus/',views.contactus,name="contactus"),
path('savemessage/',views.savemessage,name="savemessage"),
path('signuppage/',views.signuppage,name="signuppage"),
path('saveregistration/',views.saveregistration,name="saveregistration"),
path('signinpage/',views.signinpage,name="signinpage"),
path("cartpage",views.cartpage,name="cartpage"),


]