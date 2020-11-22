from django.shortcuts import render
from accounts.models import connection

# Create your views here.

def home(request):

    if request.user.is_authenticated:
        user = connection.objects.get(user=request.user)
        
        connections = user.connections.all()
        return render(request,"home.html",{'connections':connections})
    return render(request,"home.html")    

def game(request,username):
    return render(request,'game.html')