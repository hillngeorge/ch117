from django.contrib import admin
from django.urls import path, include
from pages.views import about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",  about, name="about"),
    path("contact", contact, name="contact"),
    path("content/", include("content.urls")),
]

# www.myportfolio.com/content/....