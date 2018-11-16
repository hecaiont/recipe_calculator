from django.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^calc_rw/', include('calc_rw.urls')),
]