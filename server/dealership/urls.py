from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('users/', views.get_users, name='users'),

    path('carmakes/', views.get_car_makes, name='get_car_makes'),
    path('carmodels/', views.get_car_models, name='get_car_models'),

    path('dealers/', views.dealers, name='dealers'),
    re_path(r'^dealers/(?P<dealer_id>\d+)/$', views.get_dealer_by_id, name='get_dealer_by_id'),
    re_path(r'^dealers/state/(?P<state>[A-Za-z]+)/$', views.get_dealers_by_state, name='get_dealers_by_state'),

    path('reviews/', views.get_dealer_reviews_all, name='get_dealer_reviews_all'),
    re_path(r'^reviews/(?P<dealer_id>\d+)/$', views.dealer_reviews, name='dealer_reviews'),

    path('analyze-review/', views.analyze_review, name='analyze_review'),
]
