from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('enrollee/', enrollee, name='enrollee'),
    path('quotas/', quotas, name='quotas'),
    path('finans/', finans, name='finans'),
    path('international_relationships/', international_relationships, name='international_relationships'),
    path('programs/', programs, name='programs'),
    path('ads/', ads, name='ads'),
    path('ads/category/<int:pk>', ads_category, name='ads_category'),
    path('ad/<int:pk>', ad, name="ad"),
    path('news/', news, name='news'),
    path('science/', science, name='science'),
    path('decree/', decree, name='decree'),
    path('magistr/', magistr, name='magistr'),
    path('regulations/', regulations, name='regulations'),
    path('news/category/<int:pk>', news_category, name='news_category'),
    path('new/<int:pk>', new, name="new"),
    path('central_department/', central_department, name="central_department"),
    path('facultets/', facultets, name="facultets"),
    path('fotos/', fotos, name="fotos"),
    path('foto/event/<int:pk>', foto, name='foto'),
    path('department/', department, name="department"),
    path('management/', management, name="management"),
    path('spirtual_education/', spirtual_education, name="spirtual_education"),
    path('external_department/', external_department, name="external_department"),
]
