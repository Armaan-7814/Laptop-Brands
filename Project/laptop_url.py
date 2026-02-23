from django.urls import include, path

from Project.Laptop_Brands import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mainpage.urls')),
]