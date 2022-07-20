
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
#from . import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('api/', include('api.urls')),
     #path('home', views.index, name='index')
     path('', TemplateView.as_view(template_name='index.html')),
]
