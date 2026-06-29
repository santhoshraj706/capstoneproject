from django.urls import path, re_path, include
from . import views

api_urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('get_cars/', views.get_cars, name='get_cars'),
    path('get_dealers/', views.get_dealers, name='get_dealers'),
    re_path(r'^get_dealers/(?P<dealer_id>\d+)/$', views.get_dealer_by_id, name='get_dealer_by_id'),
    re_path(r'^fetchDealer/(?P<dealer_id>\d+)/$', views.fetch_dealer, name='fetch_dealer'),
    path('analyze-review/', views.analyze_review, name='analyze_review'),
    re_path(r'^reviews/(?P<dealer_id>\d+)/$', views.dealer_reviews, name='dealer_reviews'),
]

djangoapp_urlpatterns = [
    path('login/', views.login_view, name='djangoapp_login'),
    path('logout/', views.logout_view, name='djangoapp_logout'),
    path('get_cars/', views.get_cars, name='djangoapp_get_cars'),
    path('get_dealers/', views.get_dealers, name='djangoapp_get_dealers'),
    re_path(r'^get_dealers/(?P<dealer_id>\d+)/$', views.get_dealer_by_id, name='djangoapp_get_dealer_by_id'),
    re_path(r'^fetchDealer/(?P<dealer_id>\d+)/$', views.fetch_dealer, name='djangoapp_fetch_dealer'),
    path('analyze-review/', views.analyze_review, name='djangoapp_analyze_review'),
    re_path(r'^reviews/(?P<dealer_id>\d+)/$', views.dealer_reviews, name='djangoapp_reviews'),
]
