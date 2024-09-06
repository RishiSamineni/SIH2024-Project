from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request,"app/index.html")

def UserLogin(request):
    return render(request,"app/login.html")

def UserRegister(request):
    return render(request,"app/sign.html")

def ClickableCards(request):
    return render(request,"app/card.html")

def DS_with_Teachers(request):
    return render(request,"app/teacher.html")

def DS_with_AI(request):
    return render(request,"app/aiBot.html")