from django.contrib import admin
from django.urls import path,include
from . import views


app_name="user_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.user_register,name="user_register"),
    path('login/',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    path('add/',views.addpost,name="addpost"),
    path('postdetails/',views.posts,name="posts"),

]