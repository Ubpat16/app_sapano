from django.urls import path
from .views import HomepageView, StakeView, EPOSView, P2PView, registeruser, loginuser, logoutuser, WalletView


urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('stake/', StakeView.as_view(), name='stake'),
    path('epos/', EPOSView.as_view(), name='epos'),
    path('p2p/', P2PView.as_view(), name='p2p'),
    path('register/', registeruser, name='user_register'),
    path('login/', loginuser, name='user_login'),
    path('logout/', logoutuser, name='user_logout'),
    path('wallet/', WalletView.as_view(), name='wallet')
]