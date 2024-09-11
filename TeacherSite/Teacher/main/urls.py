from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_view, name="main"),
    path('photoGalery', photoGalery_view, name="photoGalery"),
    path('videoGalery', videoGalery_view, name="videoGalery"),
    path('educationKPK', educationKPK_view, name="educationKPK"),
    path('achievement', achievements_view, name="achievement"),
    path('Studentachievement', StudentAchievements_view, name="Studentachievement"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)