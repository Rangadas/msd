from django.shortcuts import render

# Create your views here.
def newhomepage(req):
    return render(req,"newhome.html")
