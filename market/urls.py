from django.urls import path, include
from . import views
from market.views import rating_view, rateing_value

urlpatterns = [
    path('', views.index, name='index'),
    path('market_posts/', views.PostList.as_view(), name='market_posts'),
    path('market/<slug:slug>/', views.PostDetail.as_view(),
         name='post_detail'),
    path('market/rate/', rateing_value, name='rateing_value'),
]
