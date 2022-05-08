from django.urls import path
from management.views import *


urlpatterns = [
   path('', dashboard, name='dashboard'),
   path('users/', total_users, name='users'),
   path('add-package/', add_package, name='add-package'),
   path('active-packages/', active_packages, name='active-packages'),
   path('pending-packages/', pending_packages, name='pending-packages'),
   path('expired-packages/', expired_packages, name='expired-packages'),
   path('booking-enquiry/', booking_enquiry, name='booking-enquiry'),
   path('login-view/', login_view, name='login-view'),
   
]