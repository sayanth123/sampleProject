from django.contrib import admin
from django.urls import path,include
from . import views
app_name="product_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home")
]