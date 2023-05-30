from django.shortcuts import render,redirect
from realapp.models import catdb,productdb,messagedb
from webapp.models import registrationdb
# Create your views here.
def homepage(req):
    data = catdb.objects.all()
    return render(req,"home.html",{"data":data})
def aboutpage(req):
    return render(req,"about.html")
def productpage(req,catg):
    product = productdb.objects.filter(CategoryName=catg)
    return render(req,"products.html",{"product":product})
def moredetails(req,dataid):
    data = productdb.objects.get(id = dataid)
    return render(req,"moredetails.html",{"data":data})
def contactus(req):
    return render(req,"Contactus.html")
def savemessage(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        mb = req.POST.get('phone')
        ms = req.POST.get('message')
        obj = messagedb(Name=na,Email=em,Mobile=mb,Message=ms)
        obj.save()
        return redirect(contactus)
def signuppage(req):
    return render(req,"signup.html")
def saveregistration(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        ps = req.POST.get('password')
        obj = registrationdb(Name=na,Email=em,Password=ps)
        obj.save()
        return redirect(signuppage)
def signinpage(req):
    if req.method == "POST":
        em = req.POST.get('email')
        ps = req.POST.get('password')
        if registrationdb.objects.filter(Email=em,Password=ps).exists():
            req.session['email'] = em
            req.session['password'] = ps
            return redirect(homepage)
        else:
            return redirect(signuppage)
def cartpage(req):
    return render(req,"cart.html")




