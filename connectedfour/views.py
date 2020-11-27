from django.shortcuts import render,redirect
from accounts.models import connection
from django.contrib.auth import get_user_model
# Create your views here.
model = get_user_model()
def home(request):

    if request.user.is_authenticated:
        
        return redirect('profile')
    return render(request,"home.html")    

def game(request,username):
    return render(request,'game.html')

def profile(request):
    
    if request.user.is_authenticated:
        user = connection.objects.get(user=request.user)
        
        connections = user.connections.all()
        return render(request,"profile.html",{'connections':connections,})
    return render(request,"home.html")