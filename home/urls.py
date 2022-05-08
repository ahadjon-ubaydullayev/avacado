from django.urls import path
from home.views import *


urlpatterns = [
   path('home/', home, name='home'),
   path('home-2/', home2, name='home-2'),
   path('destination/', destination, name='destination'),
   path('tour-packages/', tour_packages, name='tour-packages'),
   path('package-offer/', package_offer, name='package-offer'),
   path('package-detail/', package_detail, name='package-detail'),
   path('about/', about, name='about'),
   path('services/', services, name='services'),
   path('career/', career, name='career'),
   path('career-detail/', career_detail, name='career-detail'),
   path('tour-guide/', tour_guide, name='tour-guide'),
   path('gallery/', gallery, name='gallery'),
   path('single-page/', single_page, name='single-page'),
   path('faq/', faq_page, name='faq'),
]