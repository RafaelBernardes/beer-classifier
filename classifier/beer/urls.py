from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results', views.results, name='results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)