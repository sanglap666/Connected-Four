from django.shortcuts import render,redirect
from .models import connection
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
model = get_user_model()

# Create your views here.

def signup(request):
    form = UserCreationForm(request.POST or None)
    

    if form.is_valid():
        form.save()
        
        curr_user = model.objects.get(username=request.POST.get('username'))  
         
        user_con = connection.objects.create(user=curr_user)
        users = model.objects.all()
        for user_in_db in users:
            if user_in_db != curr_user:
                user_con.connections.add(user_in_db)
        user_con.save()        
        users_in_conn = connection.objects.all()
        for user_in_conn in users_in_conn:
            if user_in_conn != user_con:
                user_in_conn.connections.add(curr_user)
        return redirect('login')

    return render(request,"signup.html",{'form':form})    

