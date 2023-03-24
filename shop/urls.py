from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.ItemList.as_view(), name='item-list'),
    path('<int:item_id>/', views.detailedItem.as_view()),
    path('search/<str:search_query>/', views.FilteredItemList.as_view()),
    # path('post/<int:postID>/', views.detailPost   .as_view(), name='post-detail'),
    # path('post/<int:postID>/comments', views.getComments().as_view(), name='comment-section'),
]
