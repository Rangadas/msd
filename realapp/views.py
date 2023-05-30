from django.shortcuts import render,redirect
from realapp.models import catdb,productdb,messagedb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def addcategory(req):
    return render(req,"addcategory.html")
def savecategory(req):
    if req.method == "POST":
        na = req.POST.get('name')
        dn = req.POST.get('desc')
        im = req.FILES['image']
        obj = catdb(Name=na,Description=dn,Image=im)
        obj.save()
        return redirect(addcategory)
def displaycategory(req):
    data = catdb.objects.all()
    return render(req,"displaycategory.html",{"data":data})
def addproduct(req):
    data = catdb.objects.all()
    return render(req,"addproduct.html",{"data":data})
def saveproduct(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        pn= req.POST.get('pname')
        desc = req.POST.get('description')
        qnt = req.POST.get('quantity')
        rs = req.POST.get('price')
        im = req.FILES['img']
        obj = productdb(CategoryName=cn,ProductName=pn,Description=desc,Quantity=qnt,Price=rs,Image=im)
        obj.save()
        messages.success(req, "Product Saved Successfully")
        return redirect(addproduct)
def displayproduct(req):
    data = productdb.objects.all()
    return render(req,"displayproduct.html",{"data":data})
def editcategory(req,dataid):
    data = catdb.objects.get(id=dataid)
    return render(req,"editcategory.html",{"data":data})
def updatecategory(req,dataid):
    if req.method=="POST":
        na = req.POST.get('name')
        dc = req.POST.get('desc')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(Name=na,Description=dc,Image=file)
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data = catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)
def editproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = catdb.objects.all()
    return render(req, "editproduct.html", {"data": data,"da":da})
def updateproduct(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('cname')
        pn = req.POST.get('pname')
        desc = req.POST.get('description')
        qnt = req.POST.get('quantity')
        rs = req.POST.get('price')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(CategoryName=cn,ProductName=pn,Description=desc,Quantity=qnt,Price=rs,Image=file)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)
def loginpage(req):
    return render(req,"loginpage.html")
def adminlogin(req):
    if req.method=="POST":
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=passwrd)
            if user is not None:
                login(req,user)
                req.session['username'] = uname
                req.session['password'] = passwrd
                return redirect(indexpage)
            else:
                return redirect(loginpage)
    else:
           return redirect(loginpage)
def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)
def displaymessage(req):
    data = messagedb.objects.all()
    return render(req,"displaymessage.html",{"data":data})
def deletemessage(req,dataid):
    data = messagedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymessage)











