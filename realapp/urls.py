from django.urls import path
from realapp import views

urlpatterns = [
    path("indexpage/",views.indexpage,name="indexpage"),
    path("addcategory/",views.addcategory,name="addcategory"),
    path("savecategory/",views.savecategory,name="savecategory"),
    path("displaycategory/",views.displaycategory,name="displaycategory"),
    path("addproduct/",views.addproduct,name="addproduct"),
    path("saveproduct/",views.saveproduct,name="saveproduct"),
    path("displayproduct/",views.displayproduct,name="displayproduct"),
    path("editcategory/<int:dataid>/",views.editcategory,name="editcategory"),
    path("updatecategory/<int:dataid>/",views.updatecategory,name="updatecategory"),
    path("deletecategory/<int:dataid>/",views.deletecategory,name="deletecategory"),
    path("editproduct/<int:dataid>/",views.editproduct,name="editproduct"),
    path("updateproduct/<int:dataid>/",views.updateproduct,name="updateproduct"),
    path("deleteproduct/<int:dataid>/",views.deleteproduct,name="deleteproduct"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("adminlogin/",views.adminlogin,name="adminlogin"),
    path("adminlogout/",views.adminlogout,name="adminlogout"),
    path("displaymessage/",views.displaymessage,name="displaymessage"),
    path("deletemessage/<int:dataid>/",views.deletemessage,name="deletemessage"),


]