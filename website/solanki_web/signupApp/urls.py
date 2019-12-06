from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name="home"),
	path('signup/',views.userSignup,name="signup"),
	path('login/',views.userLogin,name="login"),
	path('logout/',views.userLogout,name="logout"),
	# path('welcome/',views.userProfile,name="profile")
]