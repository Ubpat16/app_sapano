from django.urls import path
from .views import HomepageView, StakeView, EPOSView, P2PView, RegisterView, SapanoLoginView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('stake/', StakeView.as_view(), name='stake'),
    path('epos/', EPOSView.as_view(), name='epos'),
    path('p2p/', P2PView.as_view(), name='p2p'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SapanoLoginView.as_view(), name='login')
]