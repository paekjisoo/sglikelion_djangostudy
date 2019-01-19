from django.conf.urls import url
from django.contrib import admin
import myapp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', myapp.views.home, name="home"),
]
