from django.urls import path
from .views import AdsView, AdsDetail, AdsUpdate, AdsDelete, ReviewUpdate, ReviewDelete, review_create, review_update, user_detail, create_ad


urlpatterns = [
   path('', AdsView.as_view(), name='ads_view'), 
   path('ads/<int:pk>', AdsDetail.as_view(), name='ad_detail'),
   path('ads/<int:pk>/update', AdsUpdate.as_view()),
   path('ads/<int:pk>/delete', AdsDelete.as_view()),
   path('ads/<int:pk>/review', review_create),
   path('review/<int:pk>/update', review_update),
   path('review/<int:pk>', ReviewDelete.as_view()),
   path('profile/', user_detail, name='user_detail'),
   path('create/', create_ad),
]