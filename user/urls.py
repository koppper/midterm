from django.urls import path
from user.views import login_view, logout_view, registration, staff

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', registration, name='register'),
    path('logout/', logout_view, name='logout'),
    path('staff/', staff, name="staff")
]
