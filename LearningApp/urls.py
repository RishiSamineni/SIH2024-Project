from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexView,name="index"),
    path("login/",views.UserLogin,name="login"),
    path("sign/",views.UserRegister,name="sign"),
    path("card/",views.ClickableCards,name="card"),
    path("teacher/",views.DS_with_Teachers,name="teacher"),
    path("aiBot/",views.DS_with_AI,name="aiBot"),
]
