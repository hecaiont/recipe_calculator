from django.urls import url, include
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^brew/', include('brew.urls')),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
]