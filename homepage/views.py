from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import User

def home(request):
    return render(request, 'home.html')

def createuser(request):
    user = User()
    post = request.POST

    if post['email'] != post['remail']:
        return render(request, 'home.html', {'error': 'your emails doesnt match'})

    # if email id is matching
    user.fname=post['fname']
    user.lname=post['lname']
    user.email=post['email']
    user.password=post['password']
    user.save()

    return HttpResponse('succesfull created you account')

def login(request):
    post = request.POST

    user = get_object_or_404(User, email=post['email'])
    print(user.password)
    if user.password==post["password"]:
        def table(request):
            return render(request,'table.html')
        

       
    return HttpResponse('we do login')
    