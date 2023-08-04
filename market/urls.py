from django.urls import path, include
from . import views
from market.views import rating_view

urlpatterns = [
    path('', views.index, name='index'),
    path('market_posts/', views.PostList.as_view(), name='market_posts'),
    path('market/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
