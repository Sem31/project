from django.urls import path
from . import views


urlpatterns = [
	path('signup/',views.user_registration,name='signup'),
    path('user-profile/', views.user_profile, name='user_profile')
]
	