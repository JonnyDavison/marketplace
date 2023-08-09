from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('market_posts/', views.PostList.as_view(), name='market_posts'),
    path('market/<slug:slug>/', views.PostDetail.as_view(),
         name='post_detail'),
    path('market/submit_review/<int:post_id>', views.submit_review,
         name='submit_review'),
]
