from django.urls import path
from .views import homepage, stake, epos, p2p, registeruser, loginuser, logoutuser


urlpatterns = [
    path('', homepage, name='home'),
    path('stake/', stake, name='stake'),
    path('epos/', epos, name='epos'),
    path('p2p/', p2p, name='p2p'),
    path('register/', registeruser, name='user_register'),
    path('login/', loginuser, name='user_login'),
    path('logout/', logoutuser, name='user_logout')
]